import pyautogui as pagui
import time as time

def clicker(key):
    pagui.keyDown(key)
    time.sleep(1)
    pagui.keyUp(key)