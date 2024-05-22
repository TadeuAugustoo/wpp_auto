from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com/")


mensagem = "to te usando pra testar (isso e do app))"

lista_contatos = ["euzinho","mazz"]



#esperando abrir
WebDriverWait(nav, 300).until(EC.presence_of_element_located((By.XPATH,'//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span')))
print("logado")
time.sleep(3)

for x in lista_contatos:
    print("clicando na lupa")
    nav.find_element('xpath','//*[@id="side"]/div[1]/div/div[2]/button/div[2]').click()
    time.sleep(2)
    print("digitando o numero")
    nav.find_element('xpath','//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(x)
    time.sleep(2)
    print("apertando enter")
    nav.find_element('xpath','//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
    time.sleep(2)
    print("colocando a mensagem no campo de envio")
    nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(mensagem)
    time.sleep(2)
    print("clicando em enviar")
    nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    time.sleep(2)

input('teste')

# WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME,"username")))