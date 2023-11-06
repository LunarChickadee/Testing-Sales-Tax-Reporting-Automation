import pyautogui
import clipboard
import time
import re
from datetime import date
import os

time.sleep(5)
###this file requires that you get these arrays out of google sheets






amount_array = [1738.12,0.00,926.68,90.00,393.39,246.80,38.00,138.60,51.00,2316.80,444.46,703.95,2744.50,332.95,522.09,1135.95,344.35,196.90,310.20,0,153.70,446.60,0,436.72,847.40,364.89,346.25,494.07,0,214.20,725.43,0,455.07,0,59.00,682.97,198.20,1366.36,70.00,620.61,796.49,332.53,91.08,503.05,911.90,85.02,1080.25,118.00,69.50,795.78,1653.07,265.12,821.93,81.70,1088.30,0,0,1395.22]



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
        
    
    
            
            





    

