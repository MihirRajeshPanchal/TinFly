from TTS import *
import os
from tkinter import filedialog

def musicfileopen():
    file= filedialog.askopenfilename(title="Select a PDF", filetype=(("MP3    Files","*.mp3"),("MP4    Files","*.mp4"),("WAV    Files","*.wav"),("All Files","*.*")))
    print(file)
    os.startfile(file)