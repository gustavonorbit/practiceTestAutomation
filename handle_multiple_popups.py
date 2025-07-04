from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

path = "D:\\newProjectAutomationTest - Selenium\\chromedriver-win64\\chromedriver.exe"
service = Service(path)
drive = Chrome(service=service)
drive.get("https://demo.guru99.com/popup.php")
drive.find_element(By.LINK_TEXT, "Click Here").click()
Allwindow = drive.window_handles
for win in Allwindow:
    drive.switch_to.window(win)
    if(drive.current_url=="https://demo.guru99.com/articles_popup.php"):
        drive.find_element(By.NAME,"emailid").send_keys("teste@email.com")
        drive.find_element(By.NAME,'btnLogin').click()
        
        print("This is my main window")
    else: 
        drive.close()
assert "Access details to demo site" in drive.page_source, "Texto não encontrado"