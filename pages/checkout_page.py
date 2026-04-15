from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

class checkout_product():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    #Click checkout
    def checkout(self):
        #If error occured here, try - print("Current URL:", self.driver.current_url)
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    #Fill out checkout information
    def checkout_information(self, user_info):
        self.wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(user_info["first_name"])
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.ID, "last-name"))).send_keys(user_info["last_name"])
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.ID, "postal-code"))).send_keys(user_info["postal_code"])
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()
        time.sleep(1)

    #Double-check product(s)
    def checkout_overview(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
        time.sleep(1)
    
    #Completing checkout
    def checkout_complete(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "back-to-products"))).click()
        time.sleep(2)
        

    