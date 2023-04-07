from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
import pandas as pd
from selenium.webdriver.support.ui import Select



def get_data(url)->list:
    browser_options = Options()
    browser_options.add_experimental_option("detach", True)
    #browser_options.headless = True

    driver = webdriver.Chrome(options=browser_options)
    driver.get(url)

    #trees_links = driver.find_elements(By.ID, "search-intro")

    trees_cats = driver.find_elements(By.CLASS_NAME,"cat-name")

    list_of_trees = []

    test_count = 0

    while(True):
        
        try:
            for cat in trees_cats:
                #click catagory on Fedcoseeds.com/trees
                time.sleep(2)
                cat.click()
                time.sleep(2)

                
                driver.back()
                time.sleep(2)
        except (NoSuchElementException):
            break
    
    

    driver.quit()





    #for tree_link in trees:
    #    tree_link.click()
       # catagory = driver.find_element(By. CLASS_NAME, "category")
       # print(catagory)
    #    driver.back()
    #    time.sleep(2)

    
    #data = 
def main():
    data = get_data("https://fedcoseeds.com/trees/")

if __name__ == '__main__':
    main()