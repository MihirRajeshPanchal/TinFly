from pickletools import string1
import pywhatkit
from datetime import datetime

now = datetime.now()
hrs=now.strftime("%H")
min=now.strftime("%M")

def whatsappmsg(phno,msgstr):
    pywhatkit.sendwhatmsg(phno,msgstr,int(hrs),int(min)+1)
