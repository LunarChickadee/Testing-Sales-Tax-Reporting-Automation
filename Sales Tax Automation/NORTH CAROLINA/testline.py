import pyautogui
import time 
import clipboard


time.sleep(4)
pyautogui.hotkey('shift','space',interval=0.1)
pyautogui.hotkey('command','c')

get_line = clipboard.paste()

line_array = get_line.split('\t')

print(test)