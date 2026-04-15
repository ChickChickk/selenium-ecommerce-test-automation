from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #Open Website
    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    #write username and password
    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
        time.sleep(1)