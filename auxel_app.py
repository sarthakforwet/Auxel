from flask import Flask, render_template, request, jsonify
from google.cloud import speech
import io
import os
import pyttsx3

# Using the other directory.
from speech_rec import main

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'auxelapp-189f0ce8883c.json'
client = speech.SpeechClient()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech', methods=['POST'])
def speech_to_text():
    transcript = main()
    engine = pyttsx3.init()

    # client = speech.TextToSpeechClient()

    # voice = client.voices().list()[0]

    # # Set the voice of the engine.
    # engine.setProperty("voice", voice.name)

    # Play the speech.
    # engine.say(transcript)
    return transcript

if __name__ == '__main__':
    app.run()