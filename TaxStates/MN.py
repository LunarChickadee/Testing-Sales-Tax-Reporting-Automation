from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
import time
import pandas as pd
from selenium.webdriver.support.ui import Select



def get_data(url)->list:
    browser_options = Options()
    browser_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=browser_options)
    driver.get(url)

    #trees_links = driver.find_elements(By.ID, "search-intro")


    time.sleep(2)

    search_box = driver.find_element(By.ID,"TableFilterBox")
    gross = driver.find_element(By.ID,"Dm-w")


    while(input()==""):
        time.sleep(2)


    
    ActionChains(driver)\
        .send_keys_to_element(search_box, "test1")\
        .send_keys_to_element(gross, "test2!")\
        .key_down(Keys.ENTER)\
        .perform()
    
    ActionBuilder(driver).clear_actions()


  
        
        
    

    list_of_trees = []

    

   






    #for tree_link in trees:
    #    tree_link.click()
       # catagory = driver.find_element(By. CLASS_NAME, "category")
       # print(catagory)
    #    driver.back()
    #    time.sleep(2)

    
    #data = 
def main():
    data = get_data("https://www.mndor.state.mn.us/tp/eservices/_/#1")

if __name__ == '__main__':
    main()