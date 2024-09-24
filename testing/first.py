from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
ait = WebDriverWait(driver, 100)
driver.find_element(By.LINK_TEXT, "Signup / Login").click()

# driver.find_element(By.NAME,"password").send_keys("admin123")
# driver.find_element(By.CLASS_NAME,"oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
# while True:
#     pass