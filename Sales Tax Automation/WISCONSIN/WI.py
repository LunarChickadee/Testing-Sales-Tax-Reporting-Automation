import pyautogui
import clipboard
import time


# fn key kept getting stuck for window changes, so I made an array to pull from 
#this is made from the Check WI sheet which makes an array of values that you paste below
#make sure you have the current version of the list of counties, and that your lookups go to the right places
#and that you have a pasted list of what counties are currently there
time.sleep(5)

values = "skip,skip,121,93.25,31.25,skip,skip,26.25,skip,skip,skip,skip,251.11,39.25,11.35,skip,12.93,skip,skip,skip,skip,70.92,skip,skip,skip,skip,140.5,skip,skip,skip,37.37,skip,18.75,skip,skip,25.25,skip,65.95,skip,skip,0,0,skip,skip,skip,skip,33.5,skip,64.5,16.25,skip,64,skip,skip,59.25,skip,skip,skip,14.25,skip,44,skip,123.25,35.5,skip,skip"
usable_values = values.split(",")

for value in usable_values:
    if value == "skip":
        pyautogui.keyUp('fn')
        pyautogui.typewrite('0.00',interval=0.03)
        pyautogui.press('tab',presses=4,interval=0.3)
    else:
        pyautogui.keyUp('fn')
        pyautogui.typewrite(value,interval=0.03)
        time.sleep(0.05)
        pyautogui.press('tab',presses=4,interval=0.3)


quit()
