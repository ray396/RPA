"""
Extraindo endereço pelos sites dos correios e salvando no excel
"""
from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoEspera

from selenium.webdriver.common.by import By

navegador = opcoesSelenium.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")
tempoEspera.sleep(3)

navegador.find_element(By.NAME, "endereco").send_keys("05892387")
tempoEspera.sleep(2)
navegador.find_element(By.NAME, "btn_pesquisar").click()
tempoEspera.sleep(3)

rua = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')[0].text
print(rua)
bairro = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')[0].text
print(bairro)
cidade = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')[0].text
print(cidade)
cep = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')[0].text
print(cep)