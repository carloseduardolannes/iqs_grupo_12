from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

###################################

### ID: 6
### Funcionalidade: entrar em um time 
#                   via código
### TEST CASE NAME: Ingressar em um 
#                   time pelo código  

###################################

def screen(teste,passo):
    driver.save_screenshot(f'teste004\{teste}_passo_{passo}.png')
    return None

t=0
teste = "teste004_entrar_time"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window() 

#Teste005 entrar em um time existente

##### Step 1 #####
passo = 1.0  
#Acessar a url: https://escritorioagil.netlify.app/
driver.get('https://escritorioagil.netlify.app/')
screen(teste,passo)
##### Step 2 #####

passo = 2.0 
#Clicando em acessar conta
driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Log in').click()
#Completando os campos: Email e Senha
driver.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys('carlos@uff.br')
driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys('1234567')
screen(teste,passo)
#Clicando no Botão entrar  
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/form/div[4]/button').click()
sleep(1)
passo = 2.1
screen(teste,passo)

##### Step 3 #####
sleep(2)
passo = 3.0
#Clicando em "Entrar em um time existente"
driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[1]/button').click()
sleep(1)
#Digitando o código do time
driver.find_element(by=By.XPATH, value="//input[@placeholder='Código Ex: SW52aX...']").send_keys('SW52aXRhdGlvbi01NDE=')
sleep(1)
passo = 3.1
screen(teste,passo)
#Clicando em "Entrar"
driver.find_element(by=By.XPATH, value='/html/body/div/div/div[1]/div[2]/div[2]/div/button').click()
sleep(1)
passo = 3.2
screen(teste,passo)
driver.close()
driver.quit()