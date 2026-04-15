import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.driver_setup import create_driver
from pages.login_page import LoginPage
from pages.product_page import select_product
from pages.checkout_page import checkout_product

driver = create_driver()
user_info = {
    "first_name": "James",
    "last_name": "Arthur",
    "postal_code": "12345"
}

try:
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    product_page = select_product(driver)
    added_product = product_page.add_product_and_verify()

    checkout_page = checkout_product(driver)
    checkout_page.checkout()
    checkout_page.checkout_information(user_info)
    checkout_page.checkout_overview()
    checkout_page.checkout_complete()

finally:
    driver.quit()

    