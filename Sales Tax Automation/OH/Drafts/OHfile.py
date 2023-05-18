import pyautogui
import clipboard
import time
import re
from datetime import date
import os

time.sleep(7)
#start on taxable 
rows = 12
row_counter = 0
tab_list = ['0','2','4','6','8','10','12','14','16','18','22','2','4','6','8','10','12','14','16','18','22','2','4','6','8','10','12','14','16','18','22','2','4','6','8','10','12','14','16','18','22','2','4','6','8','10','12','14','16','18','22','2','4','6','8','10','12','14','16','18','22','2','4','6','8','10','12','14','16','18','22','2','4','6','8','10','12','14','16','18','22','2','4','6','8','10','12','14','16','18','6','2']
#special tab 6 is 91st count or [90]
    #test that
for row in range(rows):
    #print(row_counter)
    pyautogui.hotkey('down',interval=0.05)
    pyautogui.hotkey('command','c',interval=0.05)
    taxable = clipboard.paste()

    pyautogui.hotkey('right',interval=0.05)
    pyautogui.hotkey('command','c',interval=0.05)
    liability = clipboard.paste()
    
    #get tab amount
    pyautogui.hotkey('right',interval=0.05)
    pyautogui.hotkey('command','c',interval=0.05)
    tabs = clipboard.paste()

    #reset to taxable
    pyautogui.press('left',2,interval=0.05)
    
    if len(taxable) < 2 and tabs != 18 and tabs != 22 and tabs !=6:
        row_counter += 1
        continue
    else:
        #switch to webpage
        pyautogui.hotkey("ctrl","tab", interval=0.05)
        time.sleep(0.3)

        #test if it's the start round
        if row_counter != 0:
            if int(tabs) != 18:
                #tab to next taxable
                tab_count = int(tabs)
                pyautogui.press("tab",tab_count,interval=0.05)

                #paste taxable
                pyautogui.keyUp('fn')
                pyautogui.typewrite(taxable,interval=0.05)
                #shift over one
                pyautogui.hotkey('tab',interval=0.05)
                #paste liability
                pyautogui.keyUp('fn')
                pyautogui.typewrite(liability,interval=0.05)
                #shift back to taxable
                pyautogui.hotkey('shift','tab',interval=0.05)
                #shift back to start because the program is blind
                pyautogui.keyDown('shift')
                pyautogui.press('tab',tab_count,interval=0.05)
                pyautogui.keyUp('shift')
            elif tabs == 18 and row_counter <=90:
                #paste taxable
                pyautogui.keyUp('fn')
                if len(taxable)<2:
                    taxable = '0.00'
                pyautogui.typewrite(taxable,interval=0.05)
                #shift over one
                pyautogui.hotkey('tab',interval=0.05)
                #paste liability
                pyautogui.keyUp('fn')
                if len(liability)<2:
                    liability = '0.00'
                pyautogui.typewrite(liability,interval=0.05)
                #shift back to taxable
                pyautogui.hotkey('shift','tab',interval=0.05)

                #shift to next
                pyautogui.press('tab',4,interval=0.05)
                pyautogui.hotkey('enter')
                #wait
                time.sleep(7)
                #move back to start
                pyautogui.keyDown('shift')
                tab_count = int(tabs)
                pyautogui.press('tab',22,interval=0.05)
                pyautogui.keyUp('shift')
            else: 
                 #paste taxable
                pyautogui.keyUp('fn')
                if len(taxable)<2:
                    taxable = '0.00'
                pyautogui.typewrite(taxable,interval=0.05)
                #shift over one
                pyautogui.hotkey('tab',interval=0.05)
                #paste liability
                pyautogui.keyUp('fn')
                if len(liability)<2:
                    liability = '0.00'
                pyautogui.typewrite(liability,interval=0.05)
                #shift back to taxable
                pyautogui.hotkey('shift','tab',interval=0.05)

                #shift to next
                pyautogui.press('tab',4,interval=0.05)
                pyautogui.hotkey('enter')
                #wait
                time.sleep(7)
                #move back to start
                pyautogui.keyDown('shift')
                tab_count = int(tabs)
                pyautogui.press('tab',6,interval=0.05)
                pyautogui.keyUp('shift') 
                 

        else:
            #paste taxable
            pyautogui.keyDown('fn')
            pyautogui.keyUp('fn')
            if len(taxable)<2:
                    taxable = '0.00'
            pyautogui.typewrite(taxable,interval=0.05)
            #shift over one
            pyautogui.hotkey('tab',interval=0.05)
            #paste liability
            pyautogui.keyUp('fn')
            if len(liability)<2:
                    liability = '0.00'
            pyautogui.typewrite(liability,interval=0.05)
            #shift back to taxable
            pyautogui.hotkey('shift','tab',interval=0.05)


    pyautogui.hotkey('ctrl','shift','tab')
    time.sleep(0.5)
    row_counter += 1

    if row_counter >= len(tab_list):
        print("done")
        quit()

