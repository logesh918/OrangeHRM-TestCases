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
            sample_1 = 'Admin'
            sample_2 = 'PIM'
            sample_3 = 'Leave'
            sample_4 = 'Time'
            sample_5 = 'Recruitment'
            sample_6 = 'My info'
            sample_7 = 'Performance'
            sample_8 ="dashboard" and "DASHBOARD"
            sample_9 = "Directory"
            sample_10 = 'Maintenance'
            sample_11 = 'Buzz'
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
            time.sleep(5)
            search_box.send_keys(sample_1)
            admin_login = loki.driver.find_element(by= By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]')
            admin_login.click()
            time.sleep(3)
            search_box = loki.driver.find_element(by=By.XPATH,value ='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
            search_box.click()
            time.sleep(3)
            search_box.send_keys(sample_2)
            pim_login = loki.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a')
            pim_login.click()
            time.sleep(3)
            search_box = loki.driver.find_element(by=By.XPATH,value ='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
            search_box.click()
            time.sleep(3)
            search_box.send_keys(sample_3)
            leave_in = loki.driver.find_element(by= By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li')
            leave_in.click()
            time.sleep(5)
            search_box = loki.driver.find_element(by=By.XPATH,value ='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
            search_box.click()
            time.sleep(3)
            search_box.send_keys(sample_4)
            Time_in = loki.driver.find_element(by= By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li')
            Time_in.click()
            time.sleep(5)
            search_box = loki.driver.find_element(by=By.XPATH,value ='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
            search_box.click()
            time.sleep(3)
            search_box.send_keys(sample_5)
            Recruit_in = loki.driver.find_element(by= By.XPATH,value=' //*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span')
            Recruit_in.click()
            time.sleep(5)
            search_box = loki.driver.find_element(by=By.XPATH,value ='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
            search_box.click()
            time.sleep(3)
            search_box.send_keys(sample_6)
            My_info = loki.driver.find_element(by= By.XPATH,value= '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a')
            My_info.click()
            time.sleep(5)
            search_box = loki.driver.find_element(by=By.XPATH,value ='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
            search_box.click()
            time.sleep(3)
            search_box.send_keys(sample_7)
            Perfomance = loki.driver.find_element(by= By.XPATH,value= '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a')
            Perfomance.click()
            time.sleep(5)
            search_box = loki.driver.find_element(by=By.XPATH,value ='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
            search_box.click()
            time.sleep(3)
            search_box.send_keys(sample_8)
            Dash = loki.driver.find_element(by= By.XPATH,value= '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span')
            Dash.click()
            time.sleep(5)
            search_box = loki.driver.find_element(by=By.XPATH,value ='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
            search_box.click()
            time.sleep(3)
            search_box.send_keys(sample_9)
            Directory_1 = loki.driver.find_element(by= By.XPATH,value= '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span')
            Directory_1.click()
            time.sleep(5)
            search_box = loki.driver.find_element(by=By.XPATH,value ='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
            search_box.click()
            time.sleep(3)
            search_box.send_keys(sample_10)
            Main = loki.driver.find_element(by= By.XPATH,value= '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a')
            Main.click()
            time.sleep(5)
            Main_1 = loki.driver.find_element(by=By.NAME,value='password')
            Main_1.send_keys(password)
            Main_2 = loki.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[1]/form/div[4]/button[2]')
            Main_2.click()
            time.sleep(5)
            search_box = loki.driver.find_element(by=By.XPATH,value ='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
            search_box.click()
            time.sleep(3)
            search_box.send_keys(sample_11)
            Buzz = loki.driver.find_element(by= By.XPATH,value= '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a')
            Buzz.click()
            time.sleep(5)
            







            
            
loki.login()