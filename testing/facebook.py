from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.find_element(By.NAME,"email").send_keys("sxyz@gmail.com")
driver.find_element(By.NAME,"pass").send_keys("xyz")
driver.find_element(By.NAME,"login").click()
time.sleep(10)