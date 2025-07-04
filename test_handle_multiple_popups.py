from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest 

#Cria o ambiente para teste em uma fixture ou uma área que é realizada antes do teste.
#Comando para criar fixture
@pytest.fixture 
#Cria função 'drive' para carregar o Chromedriver e abrir realizar funções no Chrome
def drive():
    #Caminho para o chromedriver
    path = "D:\\newProjectAutomationTest - Selenium\\chromedriver-win64\\chromedriver.exe"
    #Cria uma instância^ de serviço com o caminho informado no parâmetro do Service
    service = Service(path)
    #Cria as opções do chrome caso seja necessário alterações como Conta pré-logada
    options = Options()
    #Cria a instância do Chrome com o serviço e as opções
    drive = Chrome(service=service, options= options)
    #Aguarda até 10 segundos para o Chrome carregar completamente
    drive.implicitly_wait(10)
    #Envia o drive para o teste
    yield drive
    #Limpa o teste após o fim do ciclo
    drive.quit()

#Cria função para testar popup
def test_open_popup(drive):
    #Abre o site informado
    drive.get("https://demo.guru99.com/popup.php")
    #Aguarda o carregamento completo
    drive.implicitly_wait(10)
    #Clica no elemento para abrir o popup
    drive.find_element(By.LINK_TEXT, "Click Here").click()
    #Altera para a próxima janela
    Allwindow = drive.window_handles
    #Verifica todas as janelas
    for win in Allwindow:
            #altera para janela
            drive.switch_to.window(win)
            #Se estiver na página informada 
            if(drive.current_url=="https://demo.guru99.com/articles_popup.php"):
                #Envia email
                drive.find_element(By.NAME,"emailid").send_keys("teste@email.com")
                #Clica no elemento
                drive.find_element(By.NAME,'btnLogin').click()
                #finaliza o loop 
                break
    #Comando para aguardar até 10 segundos somente até o elemento ser localizado.        
    WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Access details to demo site')]")))
    #Comando para criar uma validação de informação
    assert "Access details to demo site" in drive.page_source, "Texto não encontrado na página principal!"

