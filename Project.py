from tkinter import *
from PIL import ImageTk, Image

from STT import playvideo

from pywhatkit import playonyt
from TTS import *
from STT import *
from Clicker import *
from HandDetection import *

def playvideox():
    tts("Search Button Clicked")
    text= entry1.get()
    playvideo(text)
    
def sttx():
    tts("Speak Video or Music Title")
    stt()

def gesturesx():
    tts("Gestures Recognition Activated")
    handDetect()


window=Tk() #main container object
window.title("TinFly")
#window.state("zoomed")

mic= Image.open("mic.png")
resize_image = mic.resize((25,25))
mic = ImageTk.PhotoImage(resize_image)

search= Image.open("search.png")
resize_image = search.resize((25,25))
search = ImageTk.PhotoImage(resize_image)

downloads= Image.open("downloads.png")
resize_image = downloads.resize((25,25))
downloads = ImageTk.PhotoImage(resize_image)

gestures= Image.open("gestures.png")
resize_image = gestures.resize((25,25))
gestures = ImageTk.PhotoImage(resize_image)

title= Image.open("TinFly.png")
resize_image = title.resize((170,75))
title = ImageTk.PhotoImage(resize_image)

frame = Frame(master=window,width=900,height=300)
frame.pack()

img = Image.open("background.png")
resize_image = img.resize((800,300))
img = ImageTk.PhotoImage(resize_image)

label = Label(master= frame, image = img)
label.pack()

label1 = Label(master=frame, image = title, background="#ffffff")
label1.place(x=350, y=50)

label2 = Label(master=frame, text="Search", background="#ffffff")
label2.place(x=180, y=150)
label2.config(font=('Arial', 15))

entry1 = Entry(master=frame, background="#ffffff",width=40)
entry1.place(x=300,y=155)

b1 = Button(master=frame,text="Search",image= search,command=playvideox)
b1.place(x=370,y=200)

b2 = Button(master=frame,text="Audio",image = mic, command=sttx)
b2.place(x=420,y=200)

b3 = Button(master=frame,text="Enable Gestures",image = gestures, command=gesturesx)
b3.place(x=470,y=200)

tts("Welcome To Tinfly")
window.mainloop() #displays main window


    
# rtts("Welcome.txt")
# deletefile("output.mp3")
# tts("Speak Video or Music title")
# deletefile("output.mp3")
# # stt()
# playonyt("Jugnu")
# handDetect()