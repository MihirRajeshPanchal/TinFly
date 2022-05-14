import os
from tkinter import filedialog,messagebox,colorchooser
from os import listdir
from os.path import isfile, join
from Convertor import *

def ask_directory():
    playlistdirname = filedialog.askdirectory()
    playlistfiles = [f for f in listdir(playlistdirname) if isfile(join(playlistdirname, f))]
    playlist=[playlistdirname+'/'+i for i in playlistfiles if i.endswith('.mp4'or'.wav')]
    names=[i[:-4] for i in playlist]
    for i in names:
        print(i)
    j=0
    for i in playlist:
        convertor(i,names[j]+'.mp3')
        j+=1
    for i in playlist:
        os.remove(i)
    playlist=[i for i in playlistfiles if i.endswith('.mp3'or'.wav')]
    print(playlist)