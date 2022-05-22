from doctest import master
import pywhatkit as pwt
from tkinter import *
from PIL import ImageTk, Image
from PlaySingleMusic import musicfileopen
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

def googlefun():
    tts("Google Search")
    text=query.get()
    pwt.search(text)

def infofun():
    tts("Information Search")
    text=query.get()
    try:
        draw=pwt.info(text,return_value=True)
        # print("Hi : ",draw)
        tts(draw)
        tdraw(draw)
    except:
        str="No Information about "+text
        tts(str)

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

googleimg= Image.open("Photos/google.png")
resize_image = googleimg.resize((100,100))
googleimg = ImageTk.PhotoImage(resize_image)

infoimg= Image.open("Photos/information.png")
resize_image = infoimg.resize((100,100))
infoimg = ImageTk.PhotoImage(resize_image)

guiimg = Image.open("Photos/gui.jpg")
resize_image = guiimg.resize((1920,1024))
guiimg = ImageTk.PhotoImage(resize_image)

playlistimg = Image.open("Photos/playlist.png")
resize_image = playlistimg.resize((200,200))
playlistimg = ImageTk.PhotoImage(resize_image)

musicimg = Image.open("Photos/music.png")
resize_image = musicimg.resize((100,100))
musicimg = ImageTk.PhotoImage(resize_image)

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
    profilebtn = Label(master=frame,text="Profile",image =profileimg)
    profilebtn.place(x=240,y=100)
    profiletxt=Label(master=frame,text="Profile",justify='center',font=("Helvetica"))
    profiletxt.place(x=240,y=200,width=104)
    
    musicbtn = Button(master=frame,text="Play Music",image = musicimg, command=musicfileopen)
    musicbtn.place(x=240,y=500)
    musictxt=Label(master=frame,text="Play Music",justify='center',font=("Helvetica"))
    musictxt.place(x=240,y=600,width=104)
    
    googlebtn = Button(master=frame,text="Google",image = googleimg, command=googlefun)
    googlebtn.place(x=60,y=300)
    googletxt=Label(master=frame,text="Google",justify='center',font=("Helvetica"))
    googletxt.place(x=60,y=400,width=105)
    
    infobtn = Button(master=frame,text="Information",image = infoimg, command=infofun)
    infobtn.place(x=420,y=300)
    infotxt=Label(master=frame,text="Information",justify='center',font=("Helvetica"))
    infotxt.place(x=420,y=400,width=105)
    
    gesturebtn = Button(master=frame,text="Enable Gestures",image = gestures, command=gesturesx)
    gesturebtn.place(x=40,y=800)
    gesturetxt=Label(master=frame,text="Gestures",justify='center',font=("Helvetica"))
    gesturetxt.place(x=40,y=900,width=105)
    
    downloadbtn = Button(master=frame,text="Download",image = downloads, command=downloadvideo)
    downloadbtn.place(x=240,y=800)
    downloadtxt=Label(master=frame,text="Download",justify='center',font=("Helvetica"))
    downloadtxt.place(x=240,y=900,width=105)

    whatsappbtn = Button(master=frame,text="Whatsapp",image = whatsapp, command=whatsappWindow)
    whatsappbtn.place(x=440,y=800)
    whatsapptxt=Label(master=frame,text="Whatsapp",justify='center',font=("Helvetica"))
    whatsapptxt.place(x=440,y=900,width=105)


#homescreen

query = Entry(master=frame, background="#ffffff", font=("Helvetica", 32))
query.place(x=800,y=250,width=790,height=75)
querytext=Label(master=frame,text="Search Bar",justify='center',font=("Helvetica"))
querytext.place(x=801,y=325,width=790)

searchbtn = Button(master=frame,text="Search",image = search, command=playvideox)
searchbtn.place(x=1610,y=250)
searchtext=Label(master=frame,text="Search",justify='center',font=("Helvetica"))
searchtext.place(x=1610,y=320,width=75)

audiobtn = Button(master=frame,text="Audio",image = mic, command=sttx)
audiobtn.place(x=1700,y=250)
audiotxt=Label(master=frame,text="Audio",justify='center',font=("Helvetica"))
audiotxt.place(x=1700,y=320,width=75)

playlistbtn = Button(master=frame,text="Playlist",image = playlistimg, command=ask_directory)
playlistbtn.place(x=800,y=450)
playlisttext=Label(master=frame,text="Create Playlist",justify='center',font=("Helvetica"))
playlisttext.place(x=800,y=650,width=205)

bookbtn = Button(master=frame,text="E-Book",image = bookimg, command=ebookreader)
bookbtn.place(x=1200,y=450)
booktext=Label(master=frame,text="Select E-Book",justify='center',font=("Helvetica"))
booktext.place(x=1200,y=650,width=205)

paintbtn = Button(master=frame,text="Paint",image = paintimg, command=voicedraw)
paintbtn.place(x=1600,y=450)
painttext=Label(master=frame,text="Voice Draw",justify='center',font=("Helvetica"))
painttext.place(x=1600,y=650,width=205)

drawerscreen()
tts("Welcome To Tinfly")
root.mainloop()