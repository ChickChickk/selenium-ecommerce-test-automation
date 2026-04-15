## Selenium Ecommerce Test Automation

This project is a simple end-to-end UI automation built with Selenium and Python.
It simulates a real user going through an e-commerce checkout flow — from logging in, selecting a product, adding it to the cart, and completing the purchase.

The goal of this project is to practice writing clean and structured automation code using the Page Object Model (POM), while handling common UI interactions like clicking elements, waiting for page loads, and navigating between pages.

## Overview

- Automating full checkout flow (login -> cart -> checkout -> confirmation)
- Using Selenium WebDriver for browser interaction
- Applying POM for better structure

## How to Run

`git clone https://github.com/ChickChickk/selenium-ecommerce-test-automation.git
`

`pip install -r requirements.txt
`

`python tests/main.py
`
## Test Flow

1.	Open SauceDemo website
2.	Login with valid credentials
3.	Add a product to cart
4.	Navigate to checkout
5.	Fill in user information
6.	Complete the order
7.	Verify successful checkout

## Future Improvements

- Add pytest for structured test execution 
- Implement test reports
- Add more test cases (e.g., invalid login, multiple products)
- Capture screenshots on failure



