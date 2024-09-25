from selenium import webdriver

# Step 1: Launch browser
driver = webdriver.Chrome()

# Step 2: Navigate to a secure URL
driver.get("https://automationexercise.com")

# Step 3: Check if the connection is secure (HTTPS)
if "https" in driver.current_url:
    print("Secure connection: HTTPS is being used.")
else:
    print("Insecure connection: No HTTPS.")

# Step 4: Verify if the page contains insecure content
if driver.execute_script("return window.isSecureContext"):
    print("Page is secure: No mixed content detected.")
else:
    print("Warning: Mixed content (insecure elements) detected.")

# Close the browser
driver.quit()
