# Speech Recoginition libraries
import speech_recognition as sr
import pyttsx3
from io import StringIO


# Web based libraries
# from flask import Flask, render_template, request, jsonify
# app = Flask(__name__)

# Chat Based Module
import openai

# Misc Libraries
import pandas as pd
import time
import os
from speech_rec import main
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'auxel_creds.json'
client = speech.SpeechClient()

# PYTTSX3 CLASS
class _TTS:
    '''
    Load the Engine separately to avoid the endless loop in runAndWait.
    '''
    engine = None
    rate = None
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'english+f6')
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate - 25)

    def say(self,text_):
        '''
        Speak up the provided text input.
        '''
        self.engine.say(text_)
        self.engine.runAndWait()

# CHAT APP USING OPEN AI API
class ChatApp:
    '''
    Class which instantiates the openai API and handles the chat by providing a custom input
    received form voice based commands.
    '''
    def __init__(self):
        # Setting the API key to use the OpenAI API
        openai.api_key = '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'
        self.messages = [
            {"role": "system", "content": "You are a dataframe wrangler to manipulate datasets."},
        ]
        self.flag = 0

    def chat(self, message):
        '''
        Call the chat endpoint from the API.
        '''
        if self.flag:
           print('here')
           del self.messages[-1]

        self.messages.append({"role": "user", "content": message})
        print('before response')
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        print(response)
        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})
        self.flag = 1
        return response["choices"][0]["message"]['content']
    
# AUXEL BOT
class Auxel:
    '''
    The driving class for the Auxel chatbot.
    '''
    init_flag = False
    def __init__(self):    
        self.df = pd.read_csv('data.csv')
        self.text = 'Hello'
        self.chat = ChatApp()
        out = self.chat.chat(str(self.df)+'Remember the DataFrame.')
        print(out)

    def say(self, text):
        tts = _TTS()
        tts.say(text)
        del(tts)

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('tell me what you want?')
            print('Listening...')
            audio_data = r.listen(source,timeout=5)
            try:
                self.text = r.recognize_google(audio_data)
                response_text = self.process_input_query()
                return response_text
            
            except sr.UnknownValueError:
                print('Error: Speech recognition could not understand audio.')
            except sr.RequestError as e:
                print(f'Error: Could not request results from Speech Recognition service; {e}')

    def process_input_query(self):
        print('inside process input query')
        if 'code' not in self.text:
            self.text += '. Just give me the output and do not give me the code.'

        if 'hello' in self.text or 'hey' in self.text or 'hi' in self.text:
            self.say('hello')
            return 'hello'

        if 'create' in self.text or 'table' in self.text:
             self.say('just a minute..')
             self.text += 'make the resultant dataframe comma seperated. Only give me the dataframe and no other text.'
             out = self.chat.chat(self.text)
             self.say('action performed!')
             return out

        # Code for this one not working.
        if 'bye' in self.text or 'byy' in self.text or 'by' in self.text or 'goodbye' in self.text:
            exit()

        print(self.text)
        out = self.chat.chat(self.text)

        print(out)
        
        if 'create' in self.text or 'prepare' in self.text:
            self.say('done!')
        
        else:
            self.say(out)
        
        return out
        
bot = Auxel()

# FLASK APPLICATION
# @app.route('/')
# def home():
#     return render_template('index.html', text=bot.text)

# @app.route('/listen', methods=['POST'])
def listen():
    bot.say('tell me what you want?')
    transcript = main()
    bot.text = transcript
    out = bot.process_input_query()
    return out