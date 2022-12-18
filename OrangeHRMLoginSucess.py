from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
# Create variables for login credentials.

username = "Admin"
password = "admin123"
# Install the chrome web driver from selenium. 


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver')
# Launch the browser and open the github URL in your web driver.
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

# Find the username/email field and send the username to the input field.

uname = driver.find_element(By.NAME, "username")
uname.send_keys(username)

# Find the password input field and send the password to the input field.
 
pword = driver.find_element(By.NAME, "password")
pword.send_keys(password)
time.sleep(5)
# Click sign in button to login the website.
driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
# Wait for login process to complete. 
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
# Verify that the login was successful.
time.sleep(5)
error_message = "Invalid credentials"
# Retrieve any errors found. 
errors = driver.find_elements(By.CLASS_NAME,"orangehrm-login-error")
# When errors are found, the login will fail. 
if any(error_message in e.text for e in errors): 
    print("[!] Login failed")
else:
    print("[+] Login successful")
# Close the driver
driver.close()