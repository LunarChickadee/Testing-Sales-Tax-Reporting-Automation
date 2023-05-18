from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui

driver = webdriver.Firefox()
driver.get("https://eservices.dor.nc.gov/sau/contact.jsp")

window_before = driver.window_handles[0]

while True:
    test = input("\n enter any text to continue this loop \n")
    if test != "":
        break

#print(window_before)

#driver.switch_to.window(window_before)

contact_name = "Ken Hahn"
contact_email = "fedco@fedcoseeds.com"
contact_phone = "(207) 426-9900"

time.sleep(1)

name_element = driver.find_element(By.NAME,"name")
name_element.clear()
name_element.send_keys(contact_name)

email_element = driver.find_element(By.NAME,"email")
email_element.clear()
email_element.send_keys(contact_email)

phone_element = driver.find_element(By.NAME,"phone")
phone_element.clear()
phone_element.send_keys(contact_phone)
