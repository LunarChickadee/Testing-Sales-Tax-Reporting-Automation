import pyautogui
import tkinter as tk
import clipboard
import time


#loop setup
#put cursor on WA on Tax table
#get site to input

#you could use this to assign the values in the future on the last loop
for i in range(5):  181
    time.sleep(.5)
    spot = pyautogui.position()
    print(spot)

#move to taxsheet
pyautogui.moveTo(2122,144)
pyautogui.click()
time.sleep(1)

#Starting postion
pyautogui.press('right', presses=10)


#copy current value and put it in the filter
pyautogui.hotkey('command', 'c')
pyautogui.moveTo(3169,691)
pyautogui.click()
pyautogui.click()
time.sleep(1)

text_from_table = clipboard.paste()+" County"
pyautogui.typewrite(text_from_table)
pyautogui.press("enter")
time.sleep(2)

#move to taxsheet
pyautogui.moveTo(2122,144)
pyautogui.click()
time.sleep(1)

#Get taxable
pyautogui.press('left', presses=7)
pyautogui.hotkey('command', 'c')

taxable_amount = clipboard.paste()

#reset tax table for next loop
pyautogui.press('right', presses=7)

#put text in right place
pyautogui.moveTo(2728,778)
pyautogui.click()
pyautogui.click()
time.sleep(1)
pyautogui.typewrite(taxable_amount)
#print(text_from_table)

#What row do things stop at?
GSrow = 38
real_row = GSrow-5
#start loop of the rest of these actions
for county in range(real_row):
    #move to taxsheet
    pyautogui.moveTo(2122,144)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('down')

    #copy current value and put it in the filter
    pyautogui.hotkey('command', 'c')
    pyautogui.moveTo(3169,691)
    pyautogui.click()
    pyautogui.click()
    pyautogui.press("backspace")
    time.sleep(1)

    text_from_table = clipboard.paste()+" County"
    pyautogui.typewrite(text_from_table)
    pyautogui.press("enter")
    time.sleep(2)

    #move to taxsheet
    pyautogui.moveTo(2122,144)
    pyautogui.click()
    time.sleep(1)

    #Get taxable
    pyautogui.press('left', presses=7)
    pyautogui.hotkey('command', 'c')

    taxable_amount = clipboard.paste()

    #reset tax table for next loop
    pyautogui.press('right', presses=7)

    #put text in right place

    pyautogui.moveTo(2728,778)
    pyautogui.click()
    pyautogui.click()
    pyautogui.press("backspace")
    time.sleep(1)
    pyautogui.typewrite(taxable_amount)