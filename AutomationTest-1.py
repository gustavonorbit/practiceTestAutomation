from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Caminho para o webdriver
path = "C:\\Users\\Home\\Desktop\\newProjectAutomationTest\\chromedriver-win64\\chromedriver.exe"

# Criando a instância de Service com o caminho do chromedriver
service = Service(path)

# Definindo as opções do Chrome
options = webdriver.ChromeOptions()

# Inicializando o driver com o Service e as opções
driver = webdriver.Chrome(service=service, options=options)

# Abrir Chrome
driver.get("https://thetestingworld.com/testings/")
