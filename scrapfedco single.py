from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time



def get_data(url)->list:
    browser_options = Options()
    browser_options.add_experimental_option("detach", True)
    #brower_options.headless = True

    driver = webdriver.Chrome(options=browser_options)
    driver.get(url)

    #trees_links = driver.find_elements(By.ID, "search-intro")

    cat = driver.find_element(By.CLASS_NAME,"cat-name")

    cat.click()

    item = driver.find_element(By.CLASS_NAME,"name")

    item.click()

    time.sleep(2)

    item_name = driver.find_element(By.XPATH, "//h1[@class='product-name']")

    item_text = item_name
    
    print(item_text.get_attribute('innerText'))

    price_line = driver.find_element(By.XPATH,"//td[@class='pricecell']")

    print(price_line.text)

    #next step is to take this, put it in a loop, and export the contents to a csv using
    ## https://www.geeksforgeeks.org/scrape-and-save-table-data-in-csv-file-using-selenium-in-python/?ref=rp
    

  



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