import pyautogui
import clipboard
import time

#Number of columns to look through
rows = 11

#set taxsheet x and y
taxsheetX =2094
taxsheetY = 654
#Point(x=1965, y=116)


Dont_do = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,44,45,46,47,48,49,50,51,52,53,55,56,58,60,60,61,62,63,64,66,67,69,70,71,72,74,75,78,89,95,97,101,110,112,114,119,127,129,146,147,150,153,154,157,159,54,57,59,99,91,92,93,94,95,96,97,98,99,100,101,102,105,108,110,111,112,114,115,119,121,127,128,129,146,147,150,153,154,157,159]

#set WV site x and y 
# put right next scroll bar
GAX = 2655
GAY = 503                     
#Point(x=3310, y=237)
list_to_add = []

#4 tabs to enter 
down_count = 99

for x in range(159):
    while down_count in Dont_do:
        down_count += 1
        if down_count >= 159:
            quit()
    print(down_count)


    pyautogui.moveTo(taxsheetX,taxsheetY)
    pyautogui.click()
    pyautogui.click()
    time.sleep(7)

    pyautogui.moveTo(GAX,GAY)
    pyautogui.click()
    pyautogui.typewrite(str(down_count))
    pyautogui.hotkey('enter')
    time.sleep(4)
    pyautogui.press("tab",presses=4)
    pyautogui.hotkey('enter')
    time.sleep(1)

    down_count += 1
    
    if down_count >= 159:
        quit()


