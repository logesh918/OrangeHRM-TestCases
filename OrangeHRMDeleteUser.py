from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

# Create variables for login credentials.
username = "Admin"
password = "admin123"
First_Name = "Sachin"
Last_Name = "Tendulkar"
Emp_Pass = "Mcc@1234"
Confirm_Pass ="Mcc@1234"


# Launch the browser and open the github URL in your web driver.
driver = webdriver.Chrome('chromedriver')
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)

# Find the username/email field and send the username to the input field.
uname = driver.find_element(By.NAME, "username")
uname.send_keys(username)

# Find the password input field and send the password to the input field.
pword = driver.find_element(By.NAME, "password")
pword.send_keys(password)


# Click sign in button to login the website.
driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
time.sleep(3)
 
# Retrieve any errors found. 
error_message = "Invalid credentials"
errors = driver.find_elements(By.CLASS_NAME,"orangehrm-login-error")
# When errors are found, the login will fail. 
if any(error_message in e.text for e in errors): 
    print("[!] Login failed")
else:
    print("[+] Login successful")
time.sleep(3)



#Delete Employee
driver.find_element(By.LINK_TEXT, "Employee List").click()
time.sleep(3)
search_user = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input")
search_user.send_keys("Sachin Tendulkar")
time.sleep(3)
search_button = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
time.sleep(8)
delete_button= driver.find_element(By.CLASS_NAME, "bi-trash").click()
time.sleep(5)
confirm_delete = driver.find_element(By.CLASS_NAME, "oxd-button--label-danger").click()
time.sleep(3)





WebDriverWait(driver=driver, timeout=15).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
# Close the driver
driver.close()
