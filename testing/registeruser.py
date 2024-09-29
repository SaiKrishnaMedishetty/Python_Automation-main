# Test Case 1: Register User
# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'New User Signup!' is visible
# 6. Enter name and email address
# 7. Click 'Signup' button
# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
# 9. Fill details: Title, Name, Email, Password, Date of birth
# 10. Select checkbox 'Sign up for our newsletter!'
# 11. Select checkbox 'Receive special offers from our partners!'
# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
# 13. Click 'Create Account button'
# 14. Verify that 'ACCOUNT CREATED!' is visible
# 15. Click 'Continue' button
# 16. Verify that 'Logged in as username' is visible
# 17. Click 'Delete Account' button
# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Step 1: Launch browser
driver = webdriver.Chrome()

# Step 2: Navigate to the URL
driver.get("http://automationexercise.com")

# Step 3: Verify that home page is visible
assert "Automation Exercise" in driver.title

# # Step 4: Click on 'Signup / Login' button
# driver.find_element(By.PARTIAL_LINK_TEXT, "Signup / Login").click()

# # Step 5: Verify 'New User Signup!' is visible
# assert "New User Signup!" in driver.page_source

# # Step 6: Enter name and email address
# driver.find_element(By.NAME, "name").send_keys("Test User")
# driver.find_element(By.CSS_SELECTOR, "input[data-qa=signup-email]").send_keys("testuser@example.com")

# # Step 7: Click 'Signup' button
# driver.find_element(By.CSS_SELECTOR, "button[data-qa=signup-button]").click()

# # Step 8: Verify that 'ENTER ACCOUNT INFORMATION' is visible
# assert "Enter Account Information" in driver.page_source

# # Step 9: Fill details: Title, Name, Email, Password, Date of birth
# driver.find_element(By.ID, "id_gender1").click()  # Title: Mr.
# driver.find_element(By.ID, "password").send_keys("TestPassword123")

# # Select Date of Birth
# day_dropdown = Select(driver.find_element(By.ID, "days"))
# day_dropdown.select_by_value("22")
# month_dropdown = Select(driver.find_element(By.ID, "months"))
# month_dropdown.select_by_value("6")
# year_dropdown = Select(driver.find_element(By.ID, "years"))
# year_dropdown.select_by_value("1990")

# # Step 10: Select checkbox 'Sign up for our newsletter!'
# driver.find_element(By.ID, "newsletter").click()

# # Step 11: Select checkbox 'Receive special offers from our partners!'
# driver.find_element(By.ID, "optin").click()

# # Step 12: Fill details: First name, Last name, Company, Address, etc.
# driver.find_element(By.ID, "first_name").send_keys("Test")
# driver.find_element(By.ID, "last_name").send_keys("User")
# driver.find_element(By.ID, "company").send_keys("TestCompany")
# driver.find_element(By.ID, "address1").send_keys("123 Test Street")
# driver.find_element(By.ID, "address2").send_keys("Suite 101")
# driver.find_element(By.ID, "country").send_keys("United States")
# driver.find_element(By.ID, "state").send_keys("California")
# driver.find_element(By.ID, "city").send_keys("Test City")
# driver.find_element(By.ID, "zipcode").send_keys("90001")
# driver.find_element(By.ID, "mobile_number").send_keys("1234567890")

# # Step 13: Click 'Create Account' button
# driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']").click()

# # Step 14: Verify that 'ACCOUNT CREATED!' is visible
# assert "ACCOUNT CREATED!" in driver.page_source

# # Step 15: Click 'Continue' button
# driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']").click()

# # Step 16: Verify that 'Logged in as username' is visible
# assert "Logged in as Test User" in driver.page_source

# # Step 17: Click 'Delete Account' button
# driver.find_element(By.PARTIAL_LINK_TEXT, "Delete Account").click()

# # Step 18: Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
# assert "ACCOUNT DELETED!" in driver.page_source
# driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']").click()

# # Close browser after a few seconds delay
# time.sleep(5)
# driver.quit()
