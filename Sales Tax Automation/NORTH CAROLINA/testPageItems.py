import pyautogui
import time 
import clipboard


time.sleep(4)
pyautogui.hotkey('shift','tab',interval=0.1)
pyautogui.hotkey('command','a', interval=0.01)
pyautogui.hotkey('command','c', interval=0.01)

get_line = clipboard.paste()

line_array = get_line.split('Transit 0.50% Tax')

print(line_array[1])