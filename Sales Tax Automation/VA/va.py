import pyautogui
import clipboard
import time

time.sleep(7)

#start on taxable header in VA auto
#test amount
rows = 133

#full amount
#rows = 133

for row in range(rows):
    pyautogui.hotkey('down',interval=0.05)
    pyautogui.hotkey('command','c',interval=0.05)
    time.sleep(0.05)
    taxable = clipboard.paste()
    time.sleep(0.05)

    #get exempt
    pyautogui.hotkey('right',interval=0.05)
    pyautogui.hotkey('command','c',interval=0.05)
    time.sleep(0.05)
    exempt_amt = clipboard.paste()
    time.sleep(0.05)

    #get tabcount
    pyautogui.hotkey('right',interval=0.05)
    pyautogui.hotkey('command','c',interval=0.05)
    time.sleep(0.05)
    tabcount = clipboard.paste()
    tabcount = int(tabcount)
    time.sleep(0.05)

    #reset
    pyautogui.keyDown('shift')
    pyautogui.press('tab',2,interval=0.05)
    pyautogui.keyUp('shift')
    time.sleep(0.05)

    #goto page
    pyautogui.hotkey('ctrl','tab',interval=0.1)
    time.sleep(0.05)
    
    #taxable
    if float(taxable)>0:
        pyautogui.keyDown('fn')
        pyautogui.keyUp('fn')
        pyautogui.typewrite(taxable)
        time.sleep(0.05)

    #tab to exempt
    pyautogui.press('tab',tabcount,interval=0.05)
    if float(exempt_amt)>0:
        pyautogui.keyDown('fn')
        pyautogui.keyUp('fn')
        pyautogui.typewrite(exempt_amt)
        time.sleep(0.05)
    #reset for next
    pyautogui.press('tab',3,interval=0.05)
    time.sleep(0.05)
    #back to google sheet
    pyautogui.hotkey('ctrl','shift','tab',interval=0.05)
    time.sleep(0.05)




