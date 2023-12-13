import pyautogui
import clipboard
import time
import re
from datetime import date
import os

time.sleep(5)
###this file requires that you get these arrays out of google sheets

#click on albany county to get the tabs set up






amount_array = [2083,0,1019,90,417,262,38,202,75,2489,659,1018,2838,648,538,1336,344,197,654,446,465,834,847,1450,346,745,1015,32,230,725,37,503,59,952,198,1602,70,1246,333,212,503,912,799,85,1819,197,397,910,2898,265,893,82,1174,1832]



counter = 0

#get back to the start if there's no data to put in for transit
for num in amount_array:

    
   
    pyautogui.keyUp("fn")
    pyautogui.press('tab',presses=4,interval=0.05)
    amount = str(amount_array[counter])
    pyautogui.typewrite(amount)
    pyautogui.press('tab',presses=9,interval=0.05)
    pyautogui.press("space")

    counter = counter+1



        

    
        
    
    
            
            





    

