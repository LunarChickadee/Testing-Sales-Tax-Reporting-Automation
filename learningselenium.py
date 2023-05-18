from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui

driver = webdriver.Firefox()
driver.get("https://eservices.dor.nc.gov/sau/contact.jsp")

contact_name = "Ken Hahn"
contact_email = "fedco@fedcoseeds.com"
contact_phone = "(207) 426-9900"

time.sleep(1)

name_element = driver.find_element(By.NAME,"name")
name_element.clear()
name_element.send_keys(contact_name)
pyautogui.keyDown("tab")
pyautogui.typewrite(contact_email)
pyautogui.keyDown("tab")
pyautogui.typewrite(contact_phone)


#assert "Python" in driver.title
#lem = driver.find_element(By.NAME, "q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()