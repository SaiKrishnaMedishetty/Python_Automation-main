from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the Google homepage
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Wait until the element with ID 'input' is present
wait = WebDriverWait(driver, 1000)
search_box = wait.until(EC.presence_of_element_located((By.ID, "name")))

# Enter "lenovo" in the search box
search_box.send_keys("lenovo")
while True:
    pass