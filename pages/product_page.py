from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class select_product():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    #Double-check the item
    def get_product_info(self):
        name = self.wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text
        price = self.wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_price"))).text
        
        return {
        "name": name,
        "price": price
        }

    def add_product_and_verify(self):
        #Get product name BEFORE clicking
        product_name = "Sauce Labs Fleece Jacket"

        #Click add to cart
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(2)

        #Go to cart
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)

        #Get product name in cart
        cart_item_name = self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        time.sleep(2)

        #Validate
        if product_name == cart_item_name:
            print("Product matched!")
        else:
            raise AssertionError("Product mismatch!")
        time.sleep(2)
        
        return cart_item_name
    
    