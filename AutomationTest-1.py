from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
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
driver.find_element(By.NAME,"fld_password").send_keys("pass123@")
driver.find_element(By.NAME,"fld_cpassword").send_keys("pass123@")
driver.find_element(By.NAME,"dob").send_keys("20/11/1999")
driver.find_element(By.NAME,"terms").click()
driver.find_element(By.NAME,"phone").send_keys("61992044560")
driver.find_element(By.NAME,"address").send_keys("qr 1 cs test")

#Time for wait load page
time.sleep(2)

#Click on radio button
driver.find_element(By.XPATH,"//input[@value='home']").click()

#Select option 1
select_element1 = driver.find_element(By.NAME, "sex")
select = Select(select_element1)
select.select_by_value("2")
#Select option 2 
select_element2 = driver.find_element(By.NAME,"country")
select2 = Select(select_element2)
select2.select_by_value("30")
#TIME OF 3 SECONDS
time.sleep(5)
#Select option 3
select_element3 = driver.find_element(By.NAME,"state")
select3 = Select(select_element3)
select3.select_by_value("514")
#Time of 3 Seconds
time.sleep(5)
#Select option 4
select_element4 = driver.find_element(By.NAME,"city")
select4 = Select(select_element4)
select4.select_by_value("8597")

#Enter to zipcode
driver.find_element(By.NAME,"zip").send_keys("72415420")

#click to submmit
driver.find_element(By.XPATH,"//input[@value='Sign up']").click()

#Time of 5 seconds for look results
time.sleep(5)
