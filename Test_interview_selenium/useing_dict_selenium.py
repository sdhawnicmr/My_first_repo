from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the webdriver
driver = webdriver.Chrome()

# Dictionary containing web element locators and actions
element_locators = {
    'username': {'by': By.ID, 'value': 'username', 'action': 'send_keys', 'input': 'your_username'},
    'password': {'by': By.ID, 'value': 'password', 'action': 'send_keys', 'input': 'your_password'},
    'login_button': {'by': By.ID, 'value': 'loginBtn', 'action': 'click'}
}

# Open a webpage
driver.get("https://example.com/login")

# Iterate through the dictionary and perform actions
for element, details in element_locators.items():
    web_element = driver.find_element(details['by'], details['value'])
    if details['action'] == 'send_keys':
        web_element.send_keys(details['input'])
    elif details['action'] == 'click':
        web_element.click()

# Close the browser
driver.quit()
