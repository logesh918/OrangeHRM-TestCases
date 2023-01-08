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
            Emp_search = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
            first_name = ' jack 0001 0043'
            Search_click ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]/i'
            emergency_click ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a'
            name_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
            name_key = 'RedRanger'
            relation_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
            relation_key = 'Exwife'
            home_no_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
            home_no_key = '34343434343'
            add_1 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
            mobile_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
            mobile_key ='565656566556'
            work_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
            work_key = '9090907878787'
            save_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'

            
            


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
            Emp_list = loki.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a')
            Emp_list.click()
            time.sleep(5)
            Emp_name = loki.driver.find_element(by=By.XPATH,value=Emp_search)
            Emp_name.send_keys(first_name)
            time.sleep(5)
            find_emp = loki.driver.find_element(by=By.XPATH,value=Search_click)
            find_emp.click()
            time.sleep(5)
            emergency_click_1 = loki.driver.find_element(by=By.XPATH,value=emergency_click)
            emergency_click_1.click()
            time.sleep(5)
            add_det =  loki.driver.find_element(by=By.XPATH,value=add_1)
            add_det.click()
            time.sleep(5)
            name_1 = loki.driver.find_element(by=By.XPATH,value=name_add)
            name_1.send_keys(name_key)
            time.sleep(5)
            relation_1 = loki.driver.find_element(by=By.XPATH,value=relation_add)
            relation_1.send_keys(relation_key)
            time.sleep(5)
            home_1 = loki.driver.find_element(by=By.XPATH,value=home_no_add)
            home_1.send_keys(home_no_key)
            time.sleep(5)
            mobile_1 = loki.driver.find_element(by=By.XPATH,value=mobile_add)
            mobile_1.send_keys(mobile_key)
            time.sleep(5)
            work_1 = loki.driver.find_element(by=By.XPATH,value=work_add)
            work_1.send_keys(work_key)
            time.sleep(5)
            save_details = loki.driver.find_element(by=By.XPATH,value=save_add)
            save_details.click()
            time.sleep()







loki.login()            
            