from gtts import gTTS 
import os 
import time

def rtts(filename):
    fh = open(filename, "r")
    myText = fh.read()#.replace("\n", " ")
    # Language we want to use 
    language = 'en'
    output = gTTS(text=myText, lang=language, slow=False)
    output.save("output.mp3")
    fh.close() 
    os.system("start output.mp3")
def tts(text):
    mytext = text
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("output.mp3")
    os.system("start output.mp3") 

def deletefile(filename):
    time.sleep(3)
    os.remove(filename)