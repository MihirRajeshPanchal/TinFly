import pywhatkit
from datetime import datetime
from Clicker import *
from TTS import *

now = datetime.now()
hrs=now.strftime("%H")
min=now.strftime("%M")

def whatsappmsg(phno,msgstr):
    try:        
        pywhatkit.sendwhatmsg(phno,msgstr,int(hrs),int(min)+2,tab_close=True)
        clicker("enter")
        tts("Message Delivered")
    except:
        tts("Exception Raised Send Again")