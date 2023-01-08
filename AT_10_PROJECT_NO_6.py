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
            contact = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a'
            st_1_add = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
            st_1_key = 'monaco'
            st_2_add = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
            st_2_key = 'cholamandalam'
            st_3_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
            st_3_key = 'Tanjore'
            state_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input'
            state_key = 'chennai'
            zip_code_add = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
            zip_code_key = '123456'
            home_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
            home_key = '1010101010101'
            mobile_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
            mobile_key = '12121212121212'
            work_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
            work_key = '131313131313'
            work_email_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input'
            work_email_key ='bahubali@gmail.com'
            other_email_add = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input'
            other_email_key = 'ironman@gmail.com'
            saving_ct_info = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'

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
            contact_1 = loki.driver.find_element(by=By.XPATH,value=contact)
            contact_1.click()
            time.sleep(5)
            steet_1 = loki.driver.find_element(by=By.XPATH,value=st_1_add)
            steet_1.send_keys(st_1_key)
            time.sleep(5)
            steet_2 = loki.driver.find_element(by=By.XPATH,value=st_2_add)
            steet_2.send_keys(st_2_key)
            time.sleep(5)
            steet_3 = loki.driver.find_element(by=By.XPATH,value=st_3_add)
            steet_3.send_keys(st_3_key)
            time.sleep(5)
            state_21 = loki.driver.find_element(by=By.XPATH,value=state_add)
            state_21.send_keys(state_key)
            time.sleep(5)
            zip_code_entry = loki.driver.find_element(by=By.XPATH,value=zip_code_add)
            zip_code_entry.send_keys(zip_code_key)
            time.sleep(5)
            home_no = loki.driver.find_element(by=By.XPATH,value=home_add)
            home_no.send_keys(home_key)
            time.sleep(5)
            mobile_no = loki.driver.find_element(by=By.XPATH,value=mobile_add)
            mobile_no.send_keys(mobile_key)
            time.sleep(5)
            work_no = loki.driver.find_element(by=By.XPATH,value=work_add)
            work_no.send_keys(work_key)
            time.sleep(5)
            work_email = loki.driver.find_element(by=By.XPATH,value=work_email_add)
            work_email.send_keys(work_email_key)
            time.sleep(5)
            other_email = loki.driver.find_element(by=By.XPATH,value=other_email_add)
            other_email.send_keys(other_email_key)
            time.sleep(5)
            saving_1 = loki.driver.find_element(by=By.XPATH,value=saving_ct_info)
            saving_1.click()
            time.sleep(5)




loki.login()            


