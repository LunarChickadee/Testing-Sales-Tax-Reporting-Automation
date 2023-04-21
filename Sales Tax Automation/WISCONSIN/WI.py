import pyautogui
import clipboard
import time


# fn key kept getting stuck for window changes, so I made an array to pull from 
#this is made from the Check WI sheet which makes an array of values that you paste below
#make sure you have the current version of the list of counties, and that your lookups go to the right places
#and that you have a pasted list of what counties are currently there
time.sleep(5)

values = "0,453,313.65,1814.74,447.51,52.8,123.59,85,234.5,1049.62,98.15,623.67,1897.29,skip,227.88,497.58,598.58,52,92.25,17.25,68.35,448.05,skip,1132.35,skip,36.25,53.2,38.95,821.75,37.75,1067.18,350.43,skip,skip,502.23,285.95,50.75,220.25,140.56,202.15,307.29,308.2,395.58,326.2,166.2,485.49,1460.78,51.1,447.69,145.3,skip,356.93,266.1,103.5,2109.25,182.7,371.59,24.5,1241.69,110.95,109.4,65.95,275.75,704.52,19,115.25,skip,skip,skip,skip,skip,skip,skip,skip,skip"
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
