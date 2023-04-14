import pyautogui
import tkinter as tk
import clipboard
import time

#Number of columns to look through
rows = 6

#set taxsheet x and y
taxsheetX =1800
taxsheetY = 114

#set WV site x and y
WVX = 2512
WVY = 106
#Point(x=2512, y=106)

#set cursor on M2 or right above first plaintext municipality
#click in municipality box

#testnothingfound


for row in range(rows):
    #move to taxsheet

    pyautogui.moveTo(taxsheetX,taxsheetY)
    pyautogui.click()
    time.sleep(1)


    #copy current value and put it in the filter
    pyautogui.hotkey("down")
    pyautogui.hotkey('command', 'c')
    pyautogui.moveTo(WVX,WVY)
    pyautogui.click()
    time.sleep(1)
    text_from_table = clipboard.paste()
    pyautogui.typewrite(text_from_table)
    pyautogui.press("tab")
    time.sleep(2)

    #test if exists
    pyautogui.hotkey('command', 'a')
    pyautogui.hotkey('command', 'c')
    text_from_table = clipboard.paste()
    #print(text_from_table)

    if text_from_table == "0.00":
        #move to taxsheet
        pyautogui.moveTo(taxsheetX,taxsheetY)
        pyautogui.click()
        time.sleep(1)

        #to taxable column
        pyautogui.press('left', presses=9)
        pyautogui.hotkey('command', 'c')
        text_from_table = clipboard.paste()
        #reset cursor
        pyautogui.press('right', presses=9, interval=0.25)

        #go to wv site
        pyautogui.moveTo(WVX, WVY)
        pyautogui.click()
        pyautogui.typewrite(text_from_table)
        pyautogui.press('tab', presses=8, interval=0.25)
    else:
        pyautogui.hotkey('shift','tab')






    





#municipality
#Point(x=2217, y=871)

#spreadsheet
#Point(x=1898, y=122)


