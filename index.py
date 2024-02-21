"""
preenchendo form web
"""
from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoEspera

navegadorFormulario = opcoesSelenium.Chrome()
navegadorFormulario.get("https://pt.surveymonkey.com/r/WLXYDX2")
tempoEspera.sleep(2)

nome = navegadorFormulario.find_element(By.ID, "166517069")
nome.send_keys("Rayssa Ellen")
tempoEspera.sleep(1)

email = navegadorFormulario.find_element(By.ID, "166517072")
email.send_keys("rayssadantas@gmail.com")
tempoEspera.sleep(1)

telefone = navegadorFormulario.find_element(By.ID, "166517070")
telefone.send_keys("(84) 9 9201-0245")
tempoEspera.sleep(1)

sobre = navegadorFormulario.find_element(By.ID, "166517073")
sobre.send_keys("sei automatizar processo e planilhas com python")
tempoEspera.sleep(1)

btn_radio = navegadorFormulario.find_element(By.ID, "166517073")
btn_radio.send_keys("sei automatizar processo e planilhas com python")
tempoEspera.sleep(10)