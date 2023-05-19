import pyautogui
import clipboard
import time
import re
from datetime import date
import os

time.sleep(5)
###this file requires that you get these arrays out of google sheets

tab_array = [1,2,2,2,2,1,1,2,1,1,2,1,2,1,1,1,1,2,2,2,1,2,1,1,1,2,1,1,2,1,2,2,2,2,1,2,1,2,1,2,1,2,2,2,1,2,1,1,1,2,1,2,2,1,2,1,2,2,1,1,1,2,2,1,2,1,2,2,1,2,1,1,1,2,1,2,1,2,2,2,2,2,1,2,1,2,2,1,1,1,1,1,1,1,1,1,2,1,1,1]

county_array = ['skip','skip','skip','skip','Ashe','Avery','Beaufort','skip','skip','Brunswick','Buncombe','Burke','skip','Caldwell','skip','Carteret','skip','skip','Chatham','Cherokee','skip','skip','skip','Columbus','Craven','skip','Currituck','skip','Davidson','skip','skip','Durham','skip','Forsyth','skip','skip','skip','Graham','skip','skip','Guilford','skip','Harnett','skip','Henderson','skip','Hoke','skip','Iredell','Jackson','Johnston','skip','skip','skip','Lincoln','Macon','Madison','skip','McDowell','Mecklenburg','skip','skip','skip','skip','skip','skip','skip','Orange','skip','skip','skip','skip','skip','Pitt','Polk','skip','skip','Robeson','skip','Rowan','skip','skip','skip','Stanly','Stokes','skip','skip','Transylvania','skip','Union','skip','Wake','skip','skip','Watauga','skip','skip','skip','skip','Yancey']

transit_array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]

amount_array = [0.00,0.00,0.00,0.00,18.80,0.62,5.92,0.00,0.00,7.83,18.92,4.31,0.00,1.06,0.00,2.87,0.00,0.00,0.74,1.59,0.00,0.00,0.00,0.40,0.21,0.00,0.50,0.00,0.91,0.00,0.00,6.54,0.00,2.38,0.00,0.00,0.00,2.79,0.00,0.00,4.10,0.00,0.00,0.00,1.86,0.00,0.12,0.00,5.91,3.09,1.11,0.00,0.00,0.00,0.20,1.18,10.19,0.00,1.62,5.92,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.61,0.00,0.00,0.00,0.00,0.00,0.33,2.96,0.00,0.00,1.83,0.00,1.87,0.00,0.00,0.00,0.34,1.05,0.00,0.00,0.66,0.00,1.93,0.00,5.49,0.00,0.00,14.57,0.00,0.00,0.00,0.00,6.02]

transit_amount_array = [0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.19,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,2.47,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.48,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.14,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,2.08,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]


for county in county_array:
    print(county)0.0    