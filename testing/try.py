import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://automationexercise.com/")
# pagetitle = driver.title

# if pagetitle == driver.title:
#     print("web page is visible")
#     print(pagetitle)

# assert "Automation Exercise" in driver.page_source
signup = driver.find_element(By.LINK_TEXT,'Signup / Login')
signup.click()
assert "New User Signup!" in driver.page_source

driver.find_element(By.NAME,"name").send_keys("abcd99")
driver.find_element(By.XPATH,"//input[@data-qa='signup-email']").send_keys("abcd999@gmail.com")
button = driver.find_element(By.XPATH, "//button[text() = 'Signup']")
try:
 print(button.text)
except:
 None
