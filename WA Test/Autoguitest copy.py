import pyautogui
import tkinter as tk
import clipboard
import time


#loop setup
#put cursor on WA on Tax table
#get site to input

#you could use this to assign the values in the future on the last loop
for i in range(5):
    time.sleep(.5)
    spot = pyautogui.position()
    print(spot)


for n in range(10000):
    pyautogui.moveTo(2122,144)
    pyautogui.click()
    time.sleep(10)

