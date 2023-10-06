import pyautogui
import time
from pyautogui import ImageNotFoundException

#time.sleep(5)
check_button = pyautogui.screenshot() 


check_location = pyautogui.locateOnScreen("/Users/Anemone/Documents/CObutton.png")
if check_location is None:
    print("notfound")





    





