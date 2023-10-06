import pyautogui
import clipboard
import time
import re
from datetime import date
import os

#tab1 Master Taxes City Names final
#tab 2 CO cursor in filter search bar

linecount = 130
time.sleep(5)
denver_gross = 0.0
denver_exempt = 0.0
last_name = ""

for line in range(linecount):
    pyautogui.hotkey("down")
    pyautogui.hotkey('command', 'c')
    pyautogui.hotkey('command', 'c')

    city_name = clipboard.paste()
    print(city_name)
    
    if re.findall("\d",city_name):
        os.system( ' say "Error!!!" ' )
        quit()
    if len(city_name)<2 or "Strasburg Adams " in city_name or "Laporte Larimer " in city_name or "Howard Fremont" in city_name or "Durango Larimer" in city_name or "Evergreen Jefferson " in city_name and last_name != "Denver":
        continue
    

    if "Denver" in city_name:
        continue
        

    pyautogui.hotkey('ctrl','tab',interval=0.2)
    time.sleep(0.2)

    pyautogui.typewrite(city_name)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey('shift',"ctrl","tab",interval=0.1)