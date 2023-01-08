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
            Search_click ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
            Edit_id = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]/i'
            Nick_name_link = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
            Nick_name = 'millertaxi'
            other_id_1 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
            other_id_2 = '11111111'
            driver_l_No = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
            driver_l_No_1 = '222222'
            ssn_num_1 ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
            ssn_num_key = '333333333'
            sin_01 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
            sin_keys = '44444444'
            Army_01 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
            Army_keys = 'YES'
            smoker_01 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[2]/div/label/span'
            male_01 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
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
            visible_emp_id = loki.driver.find_element(by=By.XPATH,value=Edit_id)
            visible_emp_id.click()
            time.sleep(5)
            Nick_name_1 = loki.driver.find_element(by=By.XPATH,value=Nick_name_link)
            Nick_name_1.send_keys(Nick_name)
            time.sleep(5)
            other_id = loki.driver.find_element(by=By.XPATH,value=other_id_1)
            other_id.send_keys(other_id_2)
            time.sleep(5)
            DLC_NUM = loki.driver.find_element(by=By.XPATH,value=driver_l_No)
            DLC_NUM.send_keys(driver_l_No_1)
            time.sleep(5)
            SSN_001 = loki.driver.find_element(by=By.XPATH,value=ssn_num_1)
            SSN_001.send_keys(ssn_num_key)
            time.sleep(5)
            SIN_num = loki.driver.find_element(by=By.XPATH,value=sin_01)
            SIN_num.send_keys(sin_keys)
            time.sleep(5)
            Army_general = loki.driver.find_element(by=By.XPATH,value=Army_01)
            Army_general.send_keys(Army_keys)
            time.sleep(5)
            smoker_02 = loki.driver.find_element(by=By.XPATH,value=smoker_01)
            smoker_02.click()
            time.sleep(5)
            male_02 =  loki.driver.find_element(by=By.XPATH,value=male_01)
            male_02.click()
            time.sleep(5)
            



loki.login()            



