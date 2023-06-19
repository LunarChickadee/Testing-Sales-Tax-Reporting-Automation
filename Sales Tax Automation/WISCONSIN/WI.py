import pyautogui
import clipboard
import time


# fn key kept getting stuck for window changes, so I made an array to pull from 
#this is made from the Check WI sheet which makes an array of values that you paste below
#make sure you have the current version of the list of counties, and that your lookups go to the right places
#and that you have a pasted list of what counties are currently there
time.sleep(5)

values = "skip,696.31,165,869.57,230.9,skip,402.25,skip,166.25,skip,302.4,skip,3495.7,19,skip,1079.96,242.6,439.58,skip,skip,19.5,195.34,skip,41,skip,27,skip,skip,skip,skip,skip,262.95,skip,244.45,skip,849.65,25.5,83.5,83,skip,skip,0,22.2,skip,78.2,802.44,276.97,skip,30.5,skip,310.58,714.5,231.99,242.6,100.35,40.75,skip,skip,1441.52,75.6,207.57,skip,135.25,16,skip,56.5"
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
