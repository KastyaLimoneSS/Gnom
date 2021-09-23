import pyautogui as gui
import keyboard as key

a=0
b=0
def an():
    global a
    
    if a == 1:
        a=0
    elif a == 0:
        a=1
        
key.add_hotkey("a + t + e", lambda: an())
while 1 == 1:
    if a==1:
        gui.press("t")
