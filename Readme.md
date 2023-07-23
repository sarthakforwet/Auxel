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


# Creating a release

In order to publish your release, you should be aware of any changes that has been done with the UI. In sum, if MainWindow.ui file is changed,
you would first need to convert this file into its python equivalent and adjust changes accordingly. This can be achieved using the 
following command.
```{bash}
pyuic5 mainwindow.ui -o mainwindow.py
```

After this, we are ready to build the executable version of the application. This is achieved using the following command if you have 
the specifications file - 
```{bash}
pyinstaller app.spec
```

However, if you do not have the file, one can be generated and an executable can be created at the same time using the following command - 
```{bash}
pyinstaller --windowed mainwindow.py
```

As soon as we have finished with the above step, we would move on the create a setup for this application. This would be done via Installforge. For details follow the tutorial in [3].

# Debug
Whenever you want to debug the application, even in the cases where error message is not evident, just run the application without using the --windowed or -w tag.

# Issues with LangChain
If you encounter any issue with LangChain installation by pyinstaller, just copy paste the pip installed version of langchain to your dist folder and all dependencies for langchain would be resolved.

# References

1. https://www.pinecone.io/learn/series/langchain/langchain-intro/
2. https://www.youtube.com/watch?v=w-eTS8YlbZ4&t=302s
3. https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/
4. https://pyinstaller.org/en/stable/usage.html#building-macos-app-bundles