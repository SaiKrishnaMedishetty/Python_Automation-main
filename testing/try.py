from selenium import webdriver
driver=webdriver.Chrome()

result = driver.execute_script("return document.title")
print(result)  # This will print the title of the webpage
