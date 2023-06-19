import pyautogui
import clipboard
import time

#Number of columns to look through
rows = 2
#start on taxsheet above county name
#set cursor on BX or right above first plaintext municipality
#set cursor in filter
list_to_add = []
#first time:

time.sleep(4)
    #get us set up
for row in range(rows):
    
    
    #copy current       value and put it in the filter
    pyautogui.hotkey("down",interval=0.03)
    pyautogui.hotkey('command', 'c')
    pyautogui.hotkey('command', 'c')
    time.sleep(.5)
    text_from_table = clipboard.paste()
    pyautogui.press('tab', presses=3, interval=0.03)
    pyautogui.hotkey('command', 'c')
    amount_taxable = clipboard.paste()
    time.sleep(0.1)
    pyautogui.hotkey('shift','tab',interval=0.03)
    pyautogui.hotkey('shift','tab',interval=0.03)
    pyautogui.hotkey('shift','tab',interval=0.03)
    time.sleep(0.1)
    
  #switch to webpage
    pyautogui.hotkey("ctrl","tab", interval=0.05)
    time.sleep(1)

    pyautogui.keyUp("fn")
    pyautogui.typewrite(text_from_table)
    pyautogui.press('enter')
    #test if real
    time.sleep(2)
    pyautogui.press('tab', presses=9, interval=0.05)
    pyautogui.press('enter')
    time.sleep(2)       
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.keyUp("fn")
    pyautogui.typewrite(amount_taxable)
    time.sleep(2)

    pyautogui.hotkey("tab",interval=1)
    pyautogui.hotkey("tab",interval=1)
    pyautogui.hotkey("tab",interval=1)
    pyautogui.hotkey("tab",interval=1)
    pyautogui.hotkey("enter",interval=0.05)
    time.sleep(2)

    
    pyautogui.hotkey("shift","tab",presses=9,interval=0.05)
    

    pyautogui.hotkey("ctrl","shift","tab", interval=0.05)
  

    

quit()
        