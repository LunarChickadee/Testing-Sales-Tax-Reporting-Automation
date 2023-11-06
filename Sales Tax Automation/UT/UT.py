import pyautogui
import clipboard
import time
import re
from datetime import date
import os

time.sleep(5)
###this file requires that you get these arrays out panorama in the QuarterlyReporting file

#start in the filter field


county_name_array =['Cache','Garfield','Iron','Salt Lake','Sanpete','Utah','Wayne'          ]

amount_array = [59.00,1785.25,8.00,213.64,43.65,34.00,140.60]
        
pyautogui.keyUp("fn")
pyautogui.press('tab',presses=9,interval=0.5)
counter = 0

#get back to the start if there's no data to put in for transit
for county in county_name_array:

    
    pyautogui.keyUp("fn")
    county_name = str(county_name_array[counter])+" County"
    pyautogui.typewrite(county_name)
    pyautogui.press('tab',presses=3,interval=0.05)
    pyautogui.keyUp("fn")
    amount = str(amount_array[counter])
    pyautogui.typewrite(amount)
    pyautogui.press('tab',presses=3,interval=0.05)       

    counter = counter+1
        
