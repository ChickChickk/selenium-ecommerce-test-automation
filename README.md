## Selenium Ecommerce Test Automation

This project is a simple end-to-end UI automation built with Selenium and Python.
It simulates a real user going through an e-commerce checkout flow — from logging in, selecting a product, adding it to the cart, and completing the purchase.

The goal of this project is to practice writing clean and structured automation code using the Page Object Model (POM), while handling common UI interactions like clicking elements, waiting for page loads, and navigating between pages.

## Website

https://www.saucedemo.com/

<img width="1000" height="600" alt="Screenshot 2026-04-15 at 16 39 15" src="https://github.com/user-attachments/assets/e08a61df-9975-4bf6-847f-1236b9a75d6f" />

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



