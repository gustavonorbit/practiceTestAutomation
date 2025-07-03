from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#Path chrome driver
path = "D:\\newProjectAutomationTest\\chromedriver-win64\\chromedriver.exe"
#Inicialize service of Chrome
service = Service(path)
#Inicialize Chrome with service
driver = Chrome(service=service)
#Open Website
driver.get("https://thetestingworld.com")
#Variable for save element 
elemento_p_clicar = driver.find_element(By.ID,"menu494")
#Inicialize ActionChains in variable 'act'
act = ActionChains(driver)
#Click in element 
act.click(elemento_p_clicar).perform()
#Click on right button
act.context_click().perform()
#Time for view elements
time.sleep(3)

