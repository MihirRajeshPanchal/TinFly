from matplotlib.pyplot import text
from requests import delete
from TTS import *
import speech_recognition as sr
import pywhatkit as pwt
from Clicker import *
from VideoDownloader import *
import sys
import speech_recognition as sr

def stt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_text = r.listen(source,phrase_time_limit=5)
        try:
        # using google speech recognition
            text = r.recognize_google(audio_text)
            print(text)
            t=pwt.playonyt(text)
            print(t)
        except:
            tts('Couldnt Recognize your voice')
            return
def playvideo(video):
    pwt.playonyt(video)
