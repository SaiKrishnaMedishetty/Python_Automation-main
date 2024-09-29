import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Selenium")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
links = driver.find_elements(By.XPATH, "//a[contains(text(), 'Selenium')]")

for i in links:
    i.click()

winid = driver.window_handles
driver.switch_to.window(winid[3])

   

time.sleep(10)
driver.close()
