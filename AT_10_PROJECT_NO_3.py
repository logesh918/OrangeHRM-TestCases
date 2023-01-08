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
            sample_2 = 'PIM'
            first_name = ' jack'
            middle_name = '0001'
            last_name = '0043'
            emp_id = '1212'
            demo = 'miller'
            demo_1 = 'RiderMiller43@'
            Add_1 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
            create_login = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
            create_user = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
            create_pass  = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
            create_confirm_pass = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
            create_emp_log_1 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
            save_1 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
            time.sleep(5)
            loki.driver.maximize_window()
            loki.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
            time.sleep(5)
            user_input = loki.driver.find_element(By.NAME, 'username')
            pass_input = loki.driver.find_element(By.NAME, 'password')
            time.sleep(5)
            submit_button = loki.driver.find_element(By.CLASS_NAME,value= "orangehrm-login-button")
            user_input.send_keys(user)
            pass_input.send_keys(password)
            time.sleep(5)
            submit_button.click()
            time.sleep(5)
            search_box = loki.driver.find_element(by=By.XPATH,value ='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
            search_box.click()
            time.sleep(3)
            search_box.send_keys(sample_2)
            pim_login = loki.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a')
            pim_login.click()
            time.sleep(5)
            Add_click = loki.driver.find_element(by=By.XPATH,value = Add_1)
            Add_click.click()
            time.sleep(5)
            create_button = loki.driver.find_element(by=By.XPATH,value=create_login)
            create_button.click()
            time.sleep(5)
            create_first_name = loki.driver.find_element(by=By.NAME,value='firstName')
            create_first_name.send_keys(first_name)
            time.sleep(5)
            create_middle_name = loki.driver.find_element(by=By.NAME,value='middleName')
            create_middle_name.send_keys(middle_name)
            time.sleep(5)
            create_last_name = loki.driver.find_element(by=By.NAME,value='lastName')
            create_last_name.send_keys(last_name)
            time.sleep(5)
            user_create = loki.driver.find_element(by=By.XPATH,value=create_user)
            user_create.send_keys(demo)
            time.sleep(5)
            user_pass_1 = loki.driver.find_element(by=By.XPATH,value=create_pass)
            user_pass_1.send_keys(demo_1)
            time.sleep(5)
            user_confrim_pass = loki.driver.find_element(by=By.XPATH,value= create_confirm_pass)
            user_confrim_pass.send_keys(demo_1)
            time.sleep(5)
            emp_001_id = loki.driver.find_element(by=By.XPATH,value=create_emp_log_1)
            emp_001_id.send_keys(Keys.BACK_SPACE)
            time.sleep(5)
            emp_001_id = loki.driver.find_element(by=By.XPATH,value=create_emp_log_1)
            emp_001_id.send_keys(Keys.BACK_SPACE)
            time.sleep(5)
            emp_001_id = loki.driver.find_element(by=By.XPATH,value=create_emp_log_1)
            emp_001_id.send_keys(Keys.BACK_SPACE)
            time.sleep(5)
            emp_001_id = loki.driver.find_element(by=By.XPATH,value=create_emp_log_1)
            emp_001_id.send_keys(Keys.BACK_SPACE)
            time.sleep(5)
            emp_001_id = loki.driver.find_element(by=By.XPATH,value=create_emp_log_1)
            emp_001_id.send_keys(emp_id)
            time.sleep(5)
            saving_emp_list = loki.driver.find_element(by=By.XPATH,value=save_1)
            saving_emp_list.click()
            time.sleep(5)
            
loki.login()            
            