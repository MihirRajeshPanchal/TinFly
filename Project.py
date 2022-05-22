from doctest import master
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
from Whatsapp import *

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


def whatsappWindow():
    
    def whatsappsend():
        phno=phnoentry.get()
        msg=msgentry.get()
        whatsappchecksend(phno,msg)
        
    wWindow=Toplevel(master)
    wWindow.title("Whatsapp")
    wWindow.state("zoomed")
    
    #images
    bgimg = Image.open("Photos/bg.jpg")
    resize_image = bgimg.resize((1920,1024))
    bgimg = ImageTk.PhotoImage(resize_image)

    tinflyimg = Image.open("Photos/tinfly.png")
    resize_image = tinflyimg.resize((423,150))
    tinflyimg = ImageTk.PhotoImage(resize_image)
    
    sendimg = Image.open("Photos/whatsappsend.png")
    resize_image = sendimg.resize((400,144))
    sendimg = ImageTk.PhotoImage(resize_image)
    
    whatsappframe = Frame(master=wWindow,width=1680,height=1440)
    whatsappframe.pack()    
    
    whatsappbg = Label(master= whatsappframe, image = bgimg)
    whatsappbg.pack()
    
    tinflylabel = Label(master=whatsappframe,text="TinFly",image = tinflyimg)
    tinflylabel.place(x=727,y=50)
    
    phnotext=Label(master=whatsappframe,text="Enter Phone Number",justify='center',font=("Helvetica"))
    phnotext.place(x=400,y=275,width=205)
    
    phnoentry = Entry(master=whatsappframe, background="#ffffff", font=("Helvetica", 32))
    phnoentry.place(x=800,y=250,width=790,height=75)
    
    msgtext=Label(master=whatsappframe,text="Enter Message",justify='center',font=("Helvetica"))
    msgtext.place(x=400,y=475,width=205)
    
    msgentry = Entry(master=whatsappframe, background="#ffffff", font=("Helvetica", 32))
    msgentry.place(x=800,y=450,width=790,height=200)
    
    sendbtn = Button(master=whatsappframe,text="send",image = sendimg, command=whatsappsend)
    sendbtn.place(x=750,y=750)
    
    wWindow.mainloop()
    
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

whatsapp= Image.open("Photos/whatsapp.png")
resize_image = whatsapp.resize((100,100))
whatsapp = ImageTk.PhotoImage(resize_image)

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



frame = Frame(master=root,width=1680,height=1440)
frame.pack()

guilabel = Label(master= frame, image = guiimg)
guilabel.pack()

def drawerscreen():
    gesturebtn = Button(master=frame,text="Enable Gestures",image = gestures, command=gesturesx)
    gesturebtn.place(x=40,y=800)
    downloadbtn = Button(master=frame,text="Download",image = downloads, command=downloadvideo)
    downloadbtn.place(x=240,y=800)
    whatsappbtn = Button(master=frame,text="Whatsapp",image = whatsapp, command=whatsappWindow)
    whatsappbtn.place(x=440,y=800)
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