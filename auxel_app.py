from flask import Flask, render_template, request, jsonify
from google.cloud import speech
import io
import os

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
    return main()

if __name__ == '__main__':
    app.run()