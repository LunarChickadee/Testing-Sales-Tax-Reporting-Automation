import pyautogui
import time
#you could use this to assign the values in the future on the last loop
for i in range(5):
    time.sleep(.5)
    spot = pyautogui.position()
    print(spot)

    