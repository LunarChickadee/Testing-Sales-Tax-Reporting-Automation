from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
from selenium.webdriver.support.ui import Select



def get_data(url)->list:
    browser_options = Options()
    browser_options.add_experimental_option("detach", True)
    #brower_options.headless = True

    driver = webdriver.Chrome(options=browser_options)
    driver.get(url)

    #trees_links = driver.find_elements(By.ID, "search-intro")

    trees_cats = driver.find_elements(By.CLASS_NAME,"cat-name")


    while(1):
        try:
            for cat in trees_cats:
                #click catagory on Fedcoseeds.com/trees
                cat.click()

                #get list of catagories page
                item_list = driver.find_elements(By.CLASS_NAME,"name")

                for item in item_list:    
                    #click on specific item
                    item.click()
                    time.sleep(2)

                    #get item name
                    item_name = driver.find_element(By.XPATH, "//h1[@class='product-name']")
                    #text of name
                    #print(item_name.get_attribute('innerText'))

                    #get price line
                    price_line = driver.find_element(By.XPATH,"//td[@class='pricecell']")
                    
                    #text of price line
                    #print(price_line.text)

                    driver.back()
                    time.sleep(2)
        except NoSuchElementException:
            break




    #driver.quit()





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