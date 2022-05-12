import os
from tkinter import filedialog,messagebox,colorchooser
from os import listdir
from os.path import isfile, join

def ask_directory():
    playlistdirname = filedialog.askdirectory()
    playlistfiles = [f for f in listdir(playlistdirname) if isfile(join(playlistdirname, f))]
    playlist=[i for i in playlistfiles if i.endswith('.mp3'or'.wav')]
    print(playlist)