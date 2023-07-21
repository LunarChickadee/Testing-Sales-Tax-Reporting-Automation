import pyautogui
import clipboard
import time
import re
from datetime import date
import os

time.sleep(5)
###this file requires that you get these arrays out of google sheets

tab_array = [1,2,2,2,2,1,1,2,1,1,2,1,2,1,1,1,1,2,2,2,1,2,1,1,1,2,1,1,2,1,2,2,2,2,1,2,1,2,1,2,1,2,2,2,1,2,1,1,1,2,1,2,2,1,2,1,2,2,1,1,1,2,2,1,2,1,2,2,1,2,1,1,1,2,1,2,1,2,2,2,2,2,1,2,1,2,2,1,1,1,1,1,1,1,1,1,2,1,1,1]

county_array = ['Alamance','skip','Alleghany','skip','skip','skip','skip','skip','skip','skip','Buncombe','Burke','skip','skip','skip','skip','skip','skip','Chatham','skip','skip','skip','skip','skip','Craven','skip','skip','skip','skip','skip','skip','Durham','skip','Forsyth','Franklin','skip','skip','skip','skip','skip','Guilford','skip','Harnett','Haywood','Henderson','skip','skip','Hyde','skip','Jackson','Johnston','skip','skip','skip','Lincoln','skip','skip','skip','skip','skip','skip','skip','skip','skip','skip','skip','Onslow','Orange','skip','skip','skip','skip','skip','skip','skip','skip','skip','skip','skip','Rowan','Rutherford','skip','skip','skip','skip','skip','skip','skip','skip','Union','skip','Wake','skip','skip','skip','skip','skip','skip','skip','Yancey']

transit_array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]

amount_array = [2.02,0.00,0.52,0.00,0.00,0.00,0.00,0.00,0.00,0.00,5.27,0.56,0.00,0.00,0.00,0.00,0.00,0.00,0.78,0.00,0.00,0.00,0.00,0.00,0.32,0.00,0.00,0.00,0.00,0.00,0.00,0.33,0.00,0.76,2.83,0.00,0.00,0.00,0.00,0.00,1.11,0.00,0.53,1.62,0.37,0.00,0.00,3.10,0.00,1.86,1.57,0.00,0.00,0.00,0.20,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,2.78,1.41,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,6.43,0.30,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.40,0.00,3.48,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.32]

transit_amount_array = [0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.07,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.31,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.87,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]



counter = 0

#get back to the start if there's no data to put in for transit
for county in county_array:

    
    if county == "skip":
        tab_reset_count = tab_array[counter]+transit_array[counter]
        pyautogui.keyUp("fn")
        pyautogui.press('tab',presses=tab_reset_count,interval=0.05)
    elif tab_array[counter] == 2:
        pyautogui.hotkey('tab',interval=0.05)
        amount = str(amount_array[counter])
        print (amount)
        pyautogui.keyUp("fn")
        pyautogui.typewrite(amount,interval=0.05)
        pyautogui.hotkey('tab',interval=0.05)
    else: 
        amount = str(amount_array[counter])
        print (amount)
        pyautogui.keyUp("fn")
        pyautogui.typewrite(amount,interval=0.05)
        pyautogui.hotkey('tab',interval=0.05)

    if transit_array[counter] > 0:
        #pyautogui.hotkey('tab',interval=0.05)
        transit = str(transit_amount_array[counter])
        print(transit)
        pyautogui.keyUp("fn")
        pyautogui.typewrite(transit,interval=0.05)
        pyautogui.hotkey('tab',interval=0.05)

    counter = counter+1
        
    
    
            
            





    

