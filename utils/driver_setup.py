from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
    chrome_options = Options()

    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--guest")
    #chrome_options.add_argument("--disable-save-password-bubble")
    #chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver