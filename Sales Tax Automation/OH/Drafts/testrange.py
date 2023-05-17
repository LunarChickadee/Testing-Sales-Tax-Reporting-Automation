import pyautogui
import time 
import clipboard
import random
import re

array = []
num = str(random.randint(1,9999))
print(num)
filename = 'testcopy'+num+'.txt'
addfile = open(filename,'a')
time.sleep(4)
pyautogui.hotkey('shift','tab',interval=0.1)
pyautogui.hotkey('command','a', interval=0.01)
pyautogui.hotkey('command','c', interval=0.01)

get_line = clipboard.paste()

#print(get_line)

line_array = get_line.split('Tax Liability')

line_array.pop(0)
line_array.pop(10)


#print(line_array[2])
counter = 1
for line in line_array:
    test = re.split(r"\n",line)
    counter += 1
    test2 = test[2]
    test3 = test[8]
    array.append(test2+"\n"+test3)


addfile.write(str(array))
addfile.write("\n")

