from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def get_data(url)->list:
    browser_options = Options()
    #brower_options.headless = True

    driver = webdriver.Firefox(options=browser_options)
    driver.get(url)

    #trees_links = driver.find_elements(By.ID, "search-intro")

    trees_cats = driver.find_elements(By.TAG_NAME,"a")

    for tree in trees_cats:
        driver.switch_to.new_window('tab')


    #print(trees_cats)
    



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