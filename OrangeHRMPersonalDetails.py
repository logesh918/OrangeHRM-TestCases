from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium .webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import Select


class loki():
    driver = webdriver.Chrome()



    def login():
        
            user = 'Admin'
            password= 'admin123'
            time.sleep(5)
            loki.driver.maximize_window()
            loki.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
            time.sleep(5)
            user_input = loki.driver.find_element(By.NAME, 'username')
            pass_input = loki.driver.find_element(By.NAME, 'password')
            time.sleep(5)
            submit_button = loki.driver.find_element(By.CLASS_NAME, "orangehrm-login-button")
            user_input.send_keys(user)
            pass_input.send_keys(password)
            time.sleep(5)
            submit_button.click()
            time.sleep(10)
            anchor_tag = loki.driver.find_element(by = By.LINK_TEXT, value='PIM')
            anchor_tag.click()
            time.sleep(5)
            anchor_tag_1 = loki.driver.find_element(by=By.LINK_TEXT,value='Employee List')
            time.sleep(5)
            anchor_tag_1.click()
            time.sleep(5)
            Employee_id ='A56A'
            Emp_no = loki.driver.find_element(by=By.XPATH,value= "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input")
            Emp_no.click()
            Emp_no.send_keys(Employee_id)
            time.sleep(3)
            submit = loki.driver.find_element(by = By.XPATH,value= "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
            submit.click()
            time.sleep(3)
            Edit_user = loki.driver.find_element(by = By.XPATH,value ="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]")
            Edit_user.click()
            time.sleep(5)
            nick = 'RockFort'
            Nick_name_1 = loki.driver.find_element(by = By.XPATH,value = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input")
            Nick_name_1.send_keys(nick)
            time.sleep(5)
            l_no = '1234567'
            license_1 = loki.driver.find_element(by = By.XPATH,value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input")
            license_1.send_keys(l_no)
            time.sleep(5)
            date = loki.driver.find_element(by=By.LINK_TEXT,value="License Expiry Date")
            date_1=Select(date)
            date_1.select_by_visible_text('14')
            time.sleep(5)
            marry = loki.driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div")
            marry_1=Select(marry)
            marry_1.select_by_visible_text('single')
            time.sleep(5)
            nation = loki.driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i")
            nationality_1=Select(nation)
            nationality_1.select_by_visible_text('indian')
            time.sleep(5)
           
            



            
loki.login()
