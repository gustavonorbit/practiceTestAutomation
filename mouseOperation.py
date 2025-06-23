from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "D:\\newProjectAutomationTest\\chromedriver-win64\\chromedriver.exe"
service = Service(path)
driver = Chrome(service=service)
driver.get("https://thetestingworld.com")

elemento_p_clicar = driver.find_element(By.ID,"menu494")

act = ActionChains(driver)
act.click(elemento_p_clicar).perform()
act.context_click().perform()