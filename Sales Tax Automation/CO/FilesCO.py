import pyautogui
import clipboard
import time
import re
from datetime import date
import os

#tab1 Master Taxes City Names final
#tab 2 CO cursor in filter search bar

linecount = 102
time.sleep(5)
denver_gross = 0.0
denver_exempt = 0.0
last_name = ""

for line in range(linecount):
    pyautogui.hotkey("down")
    pyautogui.hotkey('command', 'c')
    pyautogui.hotkey('command', 'c')

    city_name = clipboard.paste()
    #print(city_name)
    
    if re.findall("\d",city_name):
        os.system( ' say "Error!!!" ' )
        quit()
    if len(city_name)<2 or "Strasburg Adams " in city_name or "Laporte Larimer " in city_name or "Howard Fremont" in city_name or "Durango Larimer" in city_name or "Larimer" in city_name or "Evergreen Jefferson " in city_name and last_name != "Denver" and last_name != "Broomfield":
        continue
    
    pyautogui.press('right',presses=1)
    pyautogui.hotkey('command', 'c')
    pyautogui.hotkey('command', 'c')
    
    gross_sales = clipboard.paste()
    pyautogui.press('right',presses=2,interval=0.1)
    pyautogui.hotkey('command', 'c')
    pyautogui.hotkey('command', 'c')
    
    exempt_sales = clipboard.paste()
    pyautogui.press('left',presses=3,interval=0.1)

    if "Denver" in city_name:
        last_name = "Denver"
        denver_gross = float(denver_gross) + float(gross_sales)
        denver_exempt = float(denver_exempt) + float(exempt_sales)
        continue

    if "Broomfield" in city_name:
        last_name = "Broomfield"
        denver_gross = float(denver_gross) + float(gross_sales)
        denver_exempt = float(denver_exempt) + float(exempt_sales)
        continue

    if last_name == "Denver" and "Denver" not in city_name:
        city_name = "Denver"
        last_name = ""
        pyautogui.press("up")
        gross_sales = str(denver_gross)
        exempt_sales = str(denver_exempt)

    if last_name == "Broomfield" and "Broomfield" not in city_name:
        city_name = "Broomfield"
        last_name = ""
        pyautogui.press("up")
        gross_sales = str(denver_gross)
        exempt_sales = str(denver_exempt)
        

    if float(gross_sales) < 1:
        continue

    if "Commerce" in city_name:
        gross_sales = exempt_sales
        exempt_sales = gross_sales
    

    pyautogui.hotkey('ctrl','tab',interval=0.2)
    time.sleep(0.2)

    pyautogui.typewrite(city_name)
    pyautogui.press("enter")
    time.sleep(3)

    check_button = pyautogui.screenshot() 

    


    check_location = pyautogui.locateOnScreen("/Users/Anemone/Documents/CObutton.png")
    if check_location is None:
        pyautogui.hotkey("ctrl","shift","tab",interval=0.1)
        print(city_name + ",  "+str(gross_sales))
        continue
    pyautogui.press('tab',presses=18,interval=0.2)
    pyautogui.hotkey('enter')
    time.sleep(4)
    
    pyautogui.typewrite(gross_sales)
    pyautogui.press('tab')
    pyautogui.press('tab',presses=3,interval=0.2)
    time.sleep(1)
    pyautogui.typewrite(exempt_sales)
    pyautogui.press('tab')
    time.sleep(1)

    pyautogui.keyDown('shift')
    pyautogui.press('tab',presses=8,interval=0.2)
    pyautogui.keyUp('shift')
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.keyDown('shift')
    pyautogui.press('tab',presses=18,interval=0.1)
    pyautogui.keyUp('shift')

    pyautogui.hotkey('shift','ctrl','tab',interval=0.2)
    time.sleep(0.3)



os.system( ' say "Done!!!" ' )

