from selenium import webdriver as opcoesSelenium 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui as temporEspera

from selenium.webdriver.common.by import By

#options = opcoesSelenium.ChromeOptions()
#options.add_argument("--headless")

from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.geometry("900x550")

instrucao = Label(text = "CEP: ", font= "Arial 25")
instrucao.grid(row = 1, column = 0, sticky = "W")

campoDigitavelCEP = Entry(font="Arial 25")
campoDigitavelCEP.grid(row = 1, column = 1, sticky = "W")

def pesquisaCEP():
    options = Options()
    options.headless = True
    navegador = opcoesSelenium.Chrome(options = options)
    temporEspera.sleep(1)
    navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")
    temporEspera.sleep(2)
    #"59631220"
    cep = campoDigitavelCEP.get()
    navegador.find_element(By.NAME, "endereco").send_keys(cep)
    temporEspera.sleep(2)
    navegador.find_element(By.NAME, "btn_pesquisar").click()
    temporEspera.sleep(2)
    rua = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')[0].text
    lblRua.config(text = "Rua: " + rua)
    temporEspera.sleep(1)
    bairro = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')[0].text
    lblbairro.config(text = "Bairro: " + bairro)
    temporEspera.sleep(1)
    cidade = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')[0].text
    lblcidade.config(text = "Cidade: " + cidade)
    temporEspera.sleep(1)
    cep1 = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')[0].text
    lblcep1.config(text = "CEP: " + cep1)
    temporEspera.sleep(1)

botaoPesquisar = Button(text="Pesquisar", font="Arial 25",
                        command = pesquisaCEP)
botaoPesquisar.grid(row = 2, column = 0, columnspan = 2, sticky = "NSEW")

lblRua = Label(text = "\nRua: -", font= "Arial 25")
lblRua.grid(row = 3, column = 0, columnspan = 2, sticky = "W")

lblbairro = Label(text = "\nBairro: -", font= "Arial 25")
lblbairro.grid(row = 4, column = 0, columnspan = 2, sticky = "W")

lblcidade = Label(text = "\nCidade: -", font= "Arial 25")
lblcidade.grid(row = 5, column = 0, columnspan = 2, sticky = "W")

lblcep1 = Label(text = "\nCEP: -", font= "Arial 25")
lblcep1.grid(row = 6, column = 0, columnspan = 2, sticky = "W")

janela.mainloop()

