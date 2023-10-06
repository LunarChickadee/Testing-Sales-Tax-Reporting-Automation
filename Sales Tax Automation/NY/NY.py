import pyautogui
import clipboard
import time
import re
from datetime import date
import os

time.sleep(5)
###this file requires that you get these arrays out of google sheets






amount_array = [619,39,83,290,175,235,0,299,32,1928,165,657,979,271,447,199,49,453,68,0,409,232,20,53,134,525,103,342,0,85,329,557,533,0,330,1714,203,359,171,1138,888,177,986,39,223,163,1881,150,231,538,1024,83,744,200,464,0,815,1256]



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
        
    
    
            
            





    

