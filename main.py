from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv

class GoogleSearch:
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
    
    def navigate_to_google(self):
        self.driver.get("https://www.google.com")
        reject_cookies = self.wait.until(EC.element_to_be_clickable((By.ID, "W0wltc")))
        reject_cookies.click()
    
    def search_keyword(self, keyword):
        search_bar = self.driver.find_element(By.ID, "APjFqb")
        search_bar.send_keys(keyword)
        sleep(2)
        search_bar.send_keys(Keys.ENTER)
    
    def click_first_suggestion(self):
        self.driver.find_elements(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a')[0].click()
        sleep(2)

    def tweakers_search(self, search_item):
        tweakers_search_bar = self.driver.find_element(By.XPATH, '//*[@id="mainSearch"]/div/input')
        tweakers_search_bar.send_keys(search_item)
        sleep(2)
        tweakers_search_bar.send_keys(Keys.ENTER)
        sleep(2)
        self.driver.find_elements(By.XPATH, '//*[@id="listingContainer"]/div[2]/ul/li[1]/p[1]/a')[0].click()
        sleep(2)

        shop_name = self.driver.find_elements(By.CLASS_NAME, 'ellipsis')
        shop_list_name = []
        for shop in shop_name:
            shop_list_name.append(shop.text)
        shop_list_name_new = shop_list_name[9:]


        price_tag = self.driver.find_elements(By.CLASS_NAME, 'shop-price')
        shop_list_price = []
        for price in price_tag:
            shop_list_price.append(price.text)
        shop_list_price_new = shop_list_price[1:]

        with open('np.csv', 'w', encoding='utf-8') as file:
            try:
                for i in range(len(shop_list_name_new)):
                    csv_write = csv.writer(file)
                    csv_write.writerow([shop_list_name_new[i]])
                    csv_write.writerow([shop_list_price_new[i]])
                    if "€" in shop_list_price_new[i]:
                        print('bypassed')
                        str_price = str(shop_list_price_new)
                        str_price.replace("€", '')
            except UnicodeEncodeError:
                print(UnicodeEncodeError)

    def close_browser(self):
        self.driver.quit()


search = GoogleSearch()
search.navigate_to_google()
search.search_keyword("Tweakers")
search.click_first_suggestion()
search.tweakers_search("AMD Ryzen 5 5600X Boxed")
# search.close_browser()


