from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#Web driver path
path = "D:\\newProjectAutomationTest\\chromedriver-win64\\chromedriver.exe"


# Crete service instance with path of chromedriver
service = Service(path)

# Define chrome options
options = webdriver.ChromeOptions()

# Driver inicializing with service and options
driver = webdriver.Chrome(service=service, options=options)

# Open Chrome and go to test website
driver.get("https://thetestingworld.com/testings/")

#Interact with window of browser
driver.maximize_window()

#Enter Data to the textbox
driver.find_element(By.NAME,"fld_username").send_keys("testerQA")
driver.find_element(By.XPATH,"//input[@name='fld_email']").send_keys("testerQAemail@gmail.com")

#Click on radio button
driver.find_element(By.XPATH,"//input[@value='home']").click()

#Select option on Check Box
select_element = driver.find_element(By.NAME, "sex")
select = Select(select_element)
select.select_by_value("2")

#Time of 3 second
time.sleep(5)