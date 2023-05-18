import pyautogui
import clipboard
import time

#Number of columns to look through
rows = 5

#set taxsheet x and y
taxsheetX =1901
taxsheetY = 219
#PointPoint(x=1901, y=219)


#set WV site x and y 
# put right next scroll bar
GAX = 2738
GAY = 446                      
#Px=2738, y=446)
list_to_add = []

#set cursor on BX or right above first plaintext municipality
#set cursor in filter

#first time:

   #move to taxsheet

    #get us set up
for row in range(rows):
    #move to taxsheet

    pyautogui.moveTo(taxsheetX,taxsheetY)
    pyautogui.click()
    time.sleep(1)

    #copy current       value and put it in the filter
    pyautogui.hotkey("down")
    pyautogui.hotkey('command', 'c')
    pyautogui.hotkey('command', 'c')
    time.sleep(.5)
    text_from_table = clipboard.paste()
    pyautogui.press('tab', presses=3, interval=0.02)
    pyautogui.hotkey('command', 'c')
    amount_taxable = clipboard.paste()
    time.sleep(0.1)
    pyautogui.hotkey('shift','tab')
    pyautogui.hotkey('shift','tab')
    pyautogui.hotkey('shift','tab')
    pyautogui.hotkey('command', 'c')
    time.sleep(0.1)
    
    pyautogui.moveTo(GAX,GAY)
    pyautogui.click()
    time.sleep(0.1)

    pyautogui.typewrite(text_from_table)
    pyautogui.press('enter')
    #test if real
    time.sleep(2)
    pyautogui.press('tab', presses=9, interval=0.02)
    pyautogui.press('enter')
    time.sleep(2)       
    pyautogui.press('tab')
    time.sleep(1)

    #test if exists
    pyautogui.hotkey('command', 'c')
    time.sleep(.2)
    test_amount = clipboard.paste()
    test_int=test_amount.replace('.','')
    if test_int.isnumeric():
        test_int = 1
    else:
        test_int = 0
    time.sleep(0.1)

    print(test_int)


    if (test_amount == '0.00') or (test_int == 1):
        pyautogui.typewrite(amount_taxable)
        time.sleep(.03)
        pyautogui.press('tab', presses=4, interval=0.02)
        pyautogui.hotkey('enter')
        time.sleep(1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
    else: 
        list_to_add.append(text_from_table)
        print(list_to_add)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        pyautogui.hotkey('shift','tab')
        time.sleep(0.1)
        
   

print(list_to_add)

    

quit()

quit()

for row in range(rows):
    #move to taxsheet

    pyautogui.moveTo(taxsheetX,taxsheetY)
    pyautogui.click()
    time.sleep(1)


    #copy current value and put it in the filter
    pyautogui.hotkey("down")
    pyautogui.hotkey('command', 'c')
    pyautogui.moveTo(GAX,GAY)
    pyautogui.click()
    time.sleep(.5)
    text_from_table = clipboard.paste()
    pyautogui.typewrite(text_from_table)
    pyautogui.press('enter')

    #test if real
    time.sleep(1)
    pyautogui.press('tab', presses=9, interval=0.02)
    pyautogui.press('enter')
    pyautogui.press('tab')
    time.sleep(2)

    #test if exists
    pyautogui.hotkey('command', 'a')
    pyautogui.hotkey('command', 'c')
    text_from_table = clipboard.paste()
    print(text_from_table)

    quit()

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
        pyautogui.moveTo(GAX, GAY)
        pyautogui.click()
        pyautogui.typewrite(text_from_table)
        pyautogui.press('tab', presses=8, interval=0.25)
    else:
        pyautogui.hotkey('shift','tab')






    





#municipality
#Point(x=2217, y=871)

#spreadsheet
#Point(x=1898, y=122)


