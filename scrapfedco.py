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
    tic = time.perf_counter()
    browser_options = Options()
    browser_options.add_experimental_option("detach", True)
    #browser_options.headless = True

    driver = webdriver.Chrome(options=browser_options)
    driver.get(url)

    #trees_links = driver.find_elements(By.ID, "search-intro")

    trees_cats = driver.find_elements(By.CLASS_NAME,"cat-name")
    stop_point = len(trees_cats)-1

    list_of_trees = []

    test_count = 0

    test_stop = 1200
    
    cat_count = 0

    while(True):
        
        try:
            for cat in trees_cats:
                trees_cats = driver.find_elements(By.CLASS_NAME,"cat-name")
                #click catagory on Fedcoseeds.com/trees
                try:
                    cat = trees_cats[cat_count]
                    cat.click()
                    time.sleep(2)
                    cat_count += 1
                except(IndexError):
                    break

                #get list of catagories page
                item_list = driver.find_elements(By.CLASS_NAME,"name")

                for item in item_list:

                    #to test a specific #of times
                    test_count += 1   
                    if test_count == test_stop:
                        break
                    
                    if test_count >= 5000:
                        continue 

                    print(str(test_count)) 

                    #click on specific item
                    time.sleep(1)
                    item_text = item.get_attribute('innerText')
                    print(item_text)
                    item.click()
                    time.sleep(1)

                    #get item name
                    item_name = driver.find_element(By.XPATH, "//h1[@class='product-name']")
                    #text of name
                    #print(item_name.get_attribute('innerText'))
                    item_name = item_name.get_attribute('innerText')
                    #get price line list (sometimes there's more than one)
                    price_lines = driver.find_elements(By.XPATH,"//td[@class='pricecell']")

                    loop_count = 0

                    for price_line in price_lines:
                        
                        loop_count += 1

                        if test_count >= test_stop:
                            break
                        
                        if loop_count == 1:
                            price_line_text = price_line.text 
                        else:
                            price_line_text = price_line_text + "^" + price_line.text
                        #text of price line
                        #print(price_line.text)

                    price_dict = {
                    'Item': item_name,
                    'Price Lines': price_line_text
                    }
                
                    list_of_trees.append(price_dict)
                    

                    driver.back()
                    time.sleep(2)

                driver.back()
                time.sleep(3)

                if test_count >= test_stop:
                            break
                    
                
        except (NoSuchElementException, StaleElementReferenceException):
            break
    
    df=pd.DataFrame(list_of_trees)
    df.to_csv('listOfTrees.csv')
    #driver.quit()

    toc = time.perf_counter()
    print(f"Scraped in {toc - tic:0.4f} seconds")


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