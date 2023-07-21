The project utilizes the power of Large Language Models to provide a BLV user an ability to perform data analysis and data manipulation.

# Converting .ui file to .py file
```{bash}
$ pyuic5 mainwindow.ui -o mainwindow.py
```
# Building the application

If you are building the application for the first time.
```{bash}
$ pyinstaller --windowed --onefile app.py
```

If you already have a .spec file, do this - 
```{bash}
$ pyinstaller app.spec
```

#  Usage of Google Cloud API
The Google Cloud API Speech to Text conversion tool is directly callable using the main function from `speech_rec.py` file. As in the current version, this API is not used and thus, speech_rec.py is not used.

Either of these commands would build the application according to the provided instructions.


# API Used and Pricing
Currently the system utilizes the OpenAI API for Chatting with the user. In previous versions, we used to have Google Cloud API but as we are building the desktop version of the Application, we can work well with `pyttsx3` and `pyaudio` package for SST and TTS.

Following is the pricing distribution -

| Model        |Input Price/1kTokens | Output Price/1kTokens | Function             |
|--------------|---------------------|-----------------------| ---------------------|
| GPT-3.5 Turbo| 0.0015              | 0.002                 | Chat with User       |
| Text-Davinci | 0.015               | 0.02                  | Work with SQL Queries|


# References

1. https://www.pinecone.io/learn/series/langchain/langchain-intro/
2. https://www.youtube.com/watch?v=w-eTS8YlbZ4&t=302s