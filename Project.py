import pywhatkit as pwt
from tkinter import *
from PIL import ImageTk, Image
from TTS import *
from STT import *
from Clicker import *
from HandDetection import *
from Playlist import *
from AudioBook import *
from VoiceDraw import *
from VideoDownloader import *

root=Tk() #main container object
root.title("TinFly")
root.state("zoomed")

# functions
def sttx():
    tts("Speak Video or Music Title")
    stt()
    
def playvideox():
    tts("Search Button Clicked")
    text= query.get()
    playvideo(text)
    
def gesturesx():
    tts("Gestures Recognition Activated")
    handDetect()

def downloadvideo():
    tts("Video Download")
    text=query.get()
    t=pwt.playonyt(text,open_video=False)
    print(t)
    file_path = filedialog.askdirectory()
    videodownload(t,file_path)

#images
mic= Image.open("Photos/mic.png")
resize_image = mic.resize((70,70))
mic = ImageTk.PhotoImage(resize_image)

search= Image.open("Photos/search.png")
resize_image = search.resize((70,70))
search = ImageTk.PhotoImage(resize_image)

downloads= Image.open("Photos/downloads.png")
resize_image = downloads.resize((100,100))
downloads = ImageTk.PhotoImage(resize_image)

gestures= Image.open("Photos/gestures.png")
resize_image = gestures.resize((100,100))
gestures = ImageTk.PhotoImage(resize_image)

guiimg = Image.open("Photos/gui.jpg")
resize_image = guiimg.resize((1920,1024))
guiimg = ImageTk.PhotoImage(resize_image)

playlistimg = Image.open("Photos/playlist.png")
resize_image = playlistimg.resize((200,200))
playlistimg = ImageTk.PhotoImage(resize_image)

profileimg = Image.open("Photos/profile_icon.png")
resize_image = profileimg.resize((100,100))
profileimg = ImageTk.PhotoImage(resize_image)

bookimg = Image.open("Photos/book.png")
resize_image = bookimg.resize((200,200))
bookimg = ImageTk.PhotoImage(resize_image)

paintimg = Image.open("Photos/paint.png")
resize_image = paintimg.resize((200,200))
paintimg = ImageTk.PhotoImage(resize_image)



frame = Frame(master=root,width=900,height=300)
frame.pack()

guilabel = Label(master= frame, image = guiimg)
guilabel.pack()

def drawerscreen():
    gesturebtn = Button(master=frame,text="Enable Gestures",image = gestures, command=gesturesx)
    gesturebtn.place(x=40,y=800)
    downloadbtn = Button(master=frame,text="Download",image = downloads, command=downloadvideo)
    downloadbtn.place(x=240,y=800)
    profilebtn = Label(master=frame,text="Profile",image =profileimg)
    profilebtn.place(x=240,y=100)


#homescreen
query = Entry(master=frame, background="#ffffff", font=("Helvetica", 32))
query.place(x=800,y=250,width=790,height=75)

searchbtn = Button(master=frame,text="Search",image = search, command=playvideox)
searchbtn.place(x=1610,y=250)

audiobtn = Button(master=frame,text="Audio",image = mic, command=sttx)
audiobtn.place(x=1700,y=250)

playlistbtn = Button(master=frame,text="Playlist",image = playlistimg, command=ask_directory)
playlistbtn.place(x=800,y=450)
playlisttext=Label(master=frame,text="Create Playlist",justify='center',font=("Helvetica"))
playlisttext.place(x=800,y=660,width=205)

bookbtn = Button(master=frame,text="E-Book",image = bookimg, command=ebookreader)
bookbtn.place(x=1200,y=450)
booktext=Label(master=frame,text="Select E-Book",justify='center',font=("Helvetica"))
booktext.place(x=1200,y=660,width=205)

paintbtn = Button(master=frame,text="Paint",image = paintimg, command=voicedraw)
paintbtn.place(x=1600,y=450)
painttext=Label(master=frame,text="Voice Draw",justify='center',font=("Helvetica"))
painttext.place(x=1600,y=660,width=205)

drawerscreen()
tts("Welcome To Tinfly")
root.mainloop()