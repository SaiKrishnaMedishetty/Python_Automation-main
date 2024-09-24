from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# Initialize WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Wait up to 10 seconds for the element to be present
wait = WebDriverWait(driver, 100)
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))

# Now you can send the keys
username_field.send_keys("Admin")
