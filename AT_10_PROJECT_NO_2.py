from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium .webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import Select
from selenium .webdriver.common.action_chains import ActionChains


class loki():
    driver = webdriver.Chrome()



    def login():
        
            user = 'Admin'
            password = 'admin123'
            sample_1 = 'Admin'
            select_drop_down = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]"
            select_admin_drop_down ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/comment()'
            time.sleep(2)
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
            time.sleep(5)
            search_box.send_keys(sample_1)
            admin_login = loki.driver.find_element(by= By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]')
            admin_login.click()
            time.sleep(5)
            select_drop_1 = loki.driver.find_element(by=By.XPATH,value = select_drop_down)
            select_drop_1.click()
            time.sleep(5)
            select_admin= loki.driver.find_element(by=By.XPATH,value=select_admin_drop_down) 
            select_admin = Select(select_admin)
            select_admin.select_by_visible_text('Admin')
            time.sleep(5)
            select_admin.click()
            # action = ActionChains(loki.driver)
            # action.click(on_element=select_admin).perform()
            # time.sleep(5)
            
        
            
        
            
         
           
            


            
loki.login()            
