import pyautogui
import clipboard
import time
import re
from datetime import date
import os

###note you must be in the "continue editing" part of a saved  entry for this to work
######SETUP
    #left tab, master taxes by state
    #cursor on city names final

    #right tab IL Tax
    #cursor in Filter

    #Start Program, MAKE SURE YOUR ONE TAXSHET
today = date.today()

filename = "ILtoAdd"+str(today)
addfile = open(filename,'a')


time.sleep(4)


#Number of columns to look through
rows = 131

#set taxsheet x and y
taxsheetX =1667
taxsheetY = 115
#Point(x=1667, y=115)

#set WV site x and y
ILX = 3292
ILY = 219
#Point(x=3292, y=219)

#sets document to hold issues

#set cursor on M2 or right above first plaintext city
#click in municipality box

municipality_dict = []
final_dict = {}
need_adding_list = []

for row in range(rows):
    amount_press = 12
    print(row)
    #copy current       value and put it in the filter

    pyautogui.hotkey("down")
    pyautogui.hotkey('command', 'c')
    pyautogui.hotkey('command', 'c')
    pyautogui.keyDown('command')
    pyautogui.keyUp('command')
    time.sleep(.2)
    text_from_table = clipboard.paste()
    text_from_table = text_from_table.strip()

    #Remove spaces from weirdos
    if text_from_table == "De Land":
        text_from_table = "Deland"

    if text_from_table == 'La Grange':
        text_from_table = "Lagrange"

    if text_from_table == 'Mt Prospect':
        text_from_table = "Mount Prospect"

    if text_from_table == 'North Barrington Lake':
        text_from_table = 'North Barrington'
    
    if text_from_table == 'Lasalle':
        text_from_table == 'La Salle County'


    if len(text_from_table) > 100:
        print("copy city error")
        
        os.system('say "The process is finished copy city error."')
        quit()
    print(text_from_table)

    #if we didn't get data, let's start over, cause it's blank
    if len(text_from_table) <2:
        time.sleep(0.5)
        continue

    pyautogui.press('right',presses=1)
    pyautogui.hotkey('command', 'c')
    pyautogui.hotkey('command', 'c')
    pyautogui.keyDown('command')
    pyautogui.keyUp('command')
    time.sleep(1)
    taxable_amt = clipboard.paste()
    pyautogui.press('left',presses=1)   
    time.sleep(.5)

    #move to IL site
    pyautogui.hotkey('ctrl','tab')
    time.sleep(0.2)

    #add to filter and search

    pyautogui.keyUp('fn')
    pyautogui.typewrite(text_from_table)
    pyautogui.hotkey('enter')
    time.sleep(7)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('command', 'a')
    pyautogui.hotkey('command','c')                             
   

    pyautogui.hotkey('shift','tab')
    time.sleep(.3)


    

    check_municipalities = clipboard.paste()
    if len(check_municipalities) < 30:
        print("copy page error")
        os.system('say "The process is finished copy page error."')
        quit()

    #test_list = check_municipalities.split("8b")
    #rint(re.split('\n.+\t\t',check_municipalities)) 
    get_names_only = re.findall('\n.+\t\t',check_municipalities)
    names_with_fedco = re.findall('\n.+\t+',check_municipalities)
    #check_municipalities.split("CHANGING LOC")

    
    #print(get_names_only)

    
    #blank search came up
    if get_names_only == [] and text_from_table not in names_with_fedco:
        need_adding_list.append(text_from_table)
        
        addfile.write("\n")
        addfile.writelines(need_adding_list)
        addfile.write("\n")
        

        #move to taxsheet
        pyautogui.hotkey('ctrl','shift','tab')
        time.sleep(.5)

        continue


    #not blank search
    muni_list = []
    char_remov = ['\n','\t']

    for muni in get_names_only:
        replacement = muni.replace('\n',"")
        replacement = replacement.replace('\t',"")
        #print(replacement)

        
        muni_list.append(replacement)
   

    #if it's more than one entry, we gotta check it
    #check if DeKalb works right
    if (
        len(muni_list)>1 and text_from_table not in names_with_fedco and
        muni_list[0] != text_from_table and 
        muni_list[0] != text_from_table+" (U)" and 
        muni_list[0] != "DeKalb" and text_from_table != "La Salle" and
        text_from_table != "Godfrey" and text_from_table != "McLean" and
        text_from_table != "Peoria" and text_from_table != "Barrington Lake"
        ):

        final_dict[text_from_table] = [muni_list]

        addfile.write(str(final_dict))
        addfile.write("\n")
        
    else:
    #otherwise, let's fill it out
       # print("has only one")
       
       #these we're auto filling the second option
        if (
            text_from_table == "La Salle" or 
            text_from_table == 'Godfrey' or 
            text_from_table == "Mclean" or
            text_from_table == 'Lake Villa' or 
            text_from_table == "Mclean"
            ):

            amount_press = 14
        
        if text_from_table == 'Washington':
            amount_press = 16

        if text_from_table == 'Winnebago':
            amount_press = 20

        if text_from_table == "Peoria" or text_from_table == "McHenry":
            amount_press = 34

        #fill in the single entry
        time.sleep(2)
        pyautogui.press('tab',presses=amount_press,interval=0.1)
        pyautogui.hotkey('enter')
        time.sleep(7)
        
        #yorkville has fewer tabs because it's the last one on the list
        if text_from_table == "Yorkville":
            pyautogui.press('tab',presses=11,interval=0.1)
            pyautogui.write(taxable_amt)
            pyautogui.hotkey('tab')
            time.sleep(7)
            pyautogui.keyDown('shift')
            pyautogui.press('tab',presses=6,interval=0.1)
            pyautogui.keyUp('shift')
            pyautogui.hotkey('enter')
            time.sleep(7)
        else:
            pyautogui.press('tab',presses=13,interval=0.1)
            pyautogui.keyUp('fn')
            pyautogui.typewrite(taxable_amt)
            pyautogui.hotkey('tab')
            time.sleep(7)
            pyautogui.keyDown('shift')
            pyautogui.press('tab',presses=8,interval=0.1)
            pyautogui.keyUp('shift')
            pyautogui.hotkey('enter')
            time.sleep(7)
        
        #get back to filter
        pyautogui.press('tab',presses=5,interval=0.1)
        pyautogui.hotkey('backspace')
        time.sleep(.5)

    #move to taxsheet
    pyautogui.hotkey('ctrl','shift','tab')
    time.sleep(.5)







addfile.close()            
os.system('say "The process is finished successfully."')
print("Has Multiple Locations in search"+'\n')
print(final_dict)
print("Needs to be added"+'\n')
print(need_adding_list)
        




pyautogui.hotkey('ctrl','tab')
pyautogui.typewrite("gibberish")
pyautogui.hotkey('enter')
time.sleep(8)
pyautogui.press('tab',presses=15,interval=0.1)
pyautogui.hotkey('enter')