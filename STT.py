from matplotlib.pyplot import text
from TTS import *
import speech_recognition as sr
import pywhatkit as pwt
from Clicker import *
import sys

def stt():
    print("Speech-to-text")
    r = sr.Recognizer()
    with sr.Microphone() as source:

        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            t=pwt.playonyt(text)
            print(t)
        except:
            tts("Sorry could not recognize what you said")
            deletefile("output.mp3")
            sys.exit(0)