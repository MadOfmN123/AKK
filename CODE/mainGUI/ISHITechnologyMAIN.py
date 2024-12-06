import sys
import os
import random
import pyttsx3
import datetime
import sys
import time
import os
import pyautogui
import wikipedia
import pyjokes
import pyaudio
import webbrowser
from time import sleep
from PyQt5.QtCore import QThread
import speech_recognition as sr
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtGui

from ISHIMain import Ui_Widget

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    ui.updateMovieDynamically("speaking")
    engine.say(audio)
    engine.runAndWait()


def wishings():
    ui.updateMovieDynamically("speaking")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("ISHI : GOOD MORNING BOSS")
        speak("GOOD MORNING BOSS")
    elif hour >= 12 and hour < 17:
        print("ISHI : GOOD AFTERNOON BOSS")
        speak("GOOD AFTERNOON BOSS")
    elif hour >= 17 and hour < 21:
        print("ISHI : GOOD EVENING BOSS")
        speak("GOOD EVENING BOSS")
    else:
        print("ISHI : GOOD NIGHT BOSS")
        speak("GOOD NIGHT BOSS")


class ishiCodingClass(QThread):
    def __init__(self):
        super(ishiCodingClass, self).__init__()

    def run(self):
        self.executeISHI()

    def filterTheQueryForSpecificWord(self, queryToBeFiltered):
        queryToBeFiltered = queryToBeFiltered.replace("Ishi", '')
        query = queryToBeFiltered.replace("ishi", '')
        query = query.replace("hey", '')
        query = query.replace("can", '')
        query = query.replace("please", '')
        query = query.replace("bro", '')
        query = query.replace("pro", '')
        query = query.replace("baby")
        query = query.replace("jarvy", '')
        query = query.replace("ok", '')
        query = query.replace("now", '')
        query = query.replace("you", '')
        query = query.replace("no", '')
        query = query.replace("the", '')
        query = query.replace("to", '')
        query = query.replace("do", '')
        query = query.replace("this", '')
        return query

    def wakeupCommands(self):
        ui.updateMovieDynamically("sleeping")
        while True:
            r = sr.Recognizer
            with sr.Microphone() as source:
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
            try:
                query = r.recognize_google(audio,language='en-in')
            except:
                query = "none"
            if "wake up" in query:
                break

    def show(self):
        pass


class ishiMainClass(QThread):
    def __init__(self):
        super(ishiMainClass, self).__init__()

    def run(self):
        self.runIshi()

    def commands(self):
        ui.updateMovieDynamically("listening")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            ui.updateMovieDynamically("loading")
            print("Wait For Few Movements...")
            cmd = r.recognize_google(audio, language='eng-in')
            print(f"You Just Said:{cmd}\n")

        except Exception as e:
            print(e)
            speak("Please Repeat Again")
            cmd = "none"
        return cmd

    def runIshi(self):
        wishings()
        while True:
            self.query = self.commands().lower()

            if 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir The Time Is {strTime}")

            elif "finally sleep" in self.query:
                speak("Going to sleep,sir")
                exit()

            elif "wake up" in self.query:
                speak("Going to sleep,sir")

            elif 'hello' in self.query:
                speak("Hello sir, how are you ?")

            elif 'i am fine' in self.query:
                speak("that's great, sir")
                speak("Sir how can i help u")

            elif 'how are you' in self.query:
                speak("Perfect, sir")
                speak("Sir how can i help u")

            elif 'thank you' in self.query:
                speak("you are welcome, sir")
                speak("Sir how can i help u")

            elif 'namaste' in self.query:
                speak("namaste sir, Alaa Vunnaru")

            elif 'i am fine' in self.query:
                speak("that's great, sir")
                speak("Sir how can i help u")

            elif 'how are you' in self.query:
                speak("Perfect, sir")
                speak("Sir how can i help u")

            elif 'thank you' in self.query:
                speak("you are welcome, sir")
                speak("Sir how can i help u")

            # - PROGRAM TO SPEAK -

            elif 'open google' in self.query:
                speak("Opening Google Sir...")
                os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

            elif "wikipedia" in self.query:
                speak("Searching in Wikipedia...")
                try:
                    self.query = self.query.replace("wikipedia", "")
                    result = wikipedia.summary(self.query, sentences=1)
                    speak("According To Wikipedia...")
                    print(result)
                    speak(result)
                except:
                    speak("No Result Found Sir...")
                    print("No Result Found..")

            elif self.query.startswith('type'):
                self.query.replace('type', '')
                pyautogui.write(self.query)

            elif 'joke' in self.query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif 'exit program' in self.query:
                speak("I Am Leaving Sir...")
                os.close()

    def show(self):
        pass


startExecution = ishiMainClass()


class Ui_ISHI(QMainWindow):
    def __init__(self):
        super(Ui_ISHI, self).__init__()
        self.IshiUI = Ui_Widget()
        self.IshiUI.setupUi(self)

        self.runAllMovies()

    def updateMovieDynamically(self, state):
        if state == "speaking":
            self.IshiUI.Talking.raise_()
            self.IshiUI.Talking.show()
            self.IshiUI.reload.hide()
            self.IshiUI.listing.hide()
            self.IshiUI.reload_2.hide()

        if state == "listening":
            self.IshiUI.Talking.hide()
            self.IshiUI.reload.hide()
            self.IshiUI.listing.raise_()
            self.IshiUI.listing.show()
            self.IshiUI.reload_2.hide()

        if state == "loading":
            self.IshiUI.Talking.hide()
            self.IshiUI.reload.raise_()
            self.IshiUI.reload.show()
            self.IshiUI.listing.hide()
            self.IshiUI.reload_2.hide()

        if state == "sleeping":
            self.IshiUI.Talking.hide()
            self.IshiUI.reload.hide()
            self.IshiUI.listing.hide()
            self.IshiUI.reload_2.raise_()
            self.IshiUI.reload_2.show()

    def runAllMovies(self):
        self.IshiUI.codingMovie = QtGui.QMovie("E:/ISHI TECHNOLOGY/IMAGES/G.U.I Material/ExtraGui/B.G_Template_1.gif")
        self.IshiUI.label_4.setMovie(self.IshiUI.codingMovie)
        self.IshiUI.codingMovie.start()

        self.IshiUI.circleMovie = QtGui.QMovie("C:\\Users\\HI\\Downloads\\82ab4698e35dbb487566f3cec0503f04.gif")
        self.IshiUI.label_3.setMovie(self.IshiUI.circleMovie)
        self.IshiUI.circleMovie.start()

        self.IshiUI.talkingMovie = QtGui.QMovie("E:\\ISHI TECHNOLOGY\\IMAGES\\G.U.I Material\\VoiceReg\\Siri_1.gif")
        self.IshiUI.Talking.setMovie(self.IshiUI.talkingMovie)
        self.IshiUI.talkingMovie.start()

        self.IshiUI.loadingMovie = QtGui.QMovie("E:\\ISHI TECHNOLOGY\\IMAGES\\G.U.I Material\\VoiceReg\\Qualt.gif")
        self.IshiUI.reload.setMovie(self.IshiUI.loadingMovie)
        self.IshiUI.loadingMovie.start()

        self.IshiUI.listingMovie = QtGui.QMovie("C:\\Users\\HI\\Downloads\\6ba174bf48e9b6dc8d8bd19d13c9caa9.gif")
        self.IshiUI.listing.setMovie(self.IshiUI.listingMovie)
        self.IshiUI.listingMovie.start()

        self.IshiUI.sleepingMovie = QtGui.QMovie("C:\\Users\\HI\\Downloads\\Untitled-design-unscreen.gif")
        self.IshiUI.reload_2.setMovie(self.IshiUI.sleepingMovie)
        self.IshiUI.sleepingMovie.start()

        startExecution.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_ISHI()
    ui.show()
    sys.exit(app.exec_())


