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


    list_of_trees = []

    test_count = 0

    test_stop = 1200
    
    cat_count = 0

    pages = 6

    for i in range(pages):
        page = driver.find_element(By.XPATH,'//li[@class="last"]')
        #click catagory on trees of antiquity
        
        
        #get list of catagories page
        item_list = driver.find_elements(By.XPATH,'//*[@class="product-thumb-caption-title"]')
        price_list = driver.find_elements(By.XPATH,'//*[@class="money"]')
        for (item,price) in zip(item_list,price_list):

            #to test a specific #of times
            test_count += 1   
            if test_count == test_stop:
                break
            
            if test_count >= 5000:
                continue 

            print(str(test_count)) 

            #click on specific item
            time.sleep(1)
            item_name = item.text
            print(item_name)

        
            price_line_text = price.get_attribute('innerText')
            print(price_line_text)



            price_dict = {
            'Item': item_name,
            'Price Lines': price_line_text
            }
        
            list_of_trees.append(price_dict)

        page.click()
        time.sleep(3)
            
                

    print("making dataframe")
    df=pd.DataFrame(list_of_trees)
    df.to_csv('listOfApples.csv')
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
    data = get_data("https://www.treesofantiquity.com/collections/apple-trees")

if __name__ == '__main__':
    main()