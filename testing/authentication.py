from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Launch browser
driver = webdriver.Chrome()

# Step 2: Navigate to a site that requires basic authentication
# You can pass credentials in the URL: 'https://username:password@website.com'
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

# Step 3: Verify that the user is successfully authenticated
if "Congratulations!" in driver.page_source:
    print("Authentication Successful!")
else:
    print("Authentication Failed!")

# Step 4: Close the browser
driver.quit()
