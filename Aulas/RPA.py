import pyautogui as posicaoAbreArquivos

posicaoAbreArquivos.hotkey('win','r')

posicaoAbreArquivos.typewrite('notepad')

posicaoAbreArquivos.press('enter')

posicaoAbreArquivos.sleep(3)

posicaoAbreArquivos.typewrite('entrei atraves de codigo')

posicaoAbreArquivos.sleep(2)

fecharJanelaNotepad = posicaoAbreArquivos.getActiveWindow()

posicaoAbreArquivos.sleep(2)

fecharJanelaNotepad.close()

posicaoAbreArquivos.sleep(2)

posicaoAbreArquivos.press('tab')

posicaoAbreArquivos.sleep(2)

posicaoAbreArquivos.press('enter')


"""
Criando menu de opções para abrir o excel, word ou notepad
"""

import pyautogui
import pyautogui as escolha_opcao

opcao = pyautogui.confirm('clique no botão desejado', buttons = ['Excel', 'Word', 'Notepad'])

if opcao == 'Excel':
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('Excel')
    escolha_opcao.press('Enter')
    escolha_opcao.sleep(6)
    escolha_opcao.click(x=434, y=273)
    escolha_opcao.sleep(3)
    escolha_opcao.typewrite('Escolhi abrir o Excel')
elif opcao == 'Word':
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('winword')
    escolha_opcao.press('Enter')
    escolha_opcao.sleep(6)
    escolha_opcao.click(x=449, y=309)
    escolha_opcao.sleep(3)
    escolha_opcao.typewrite('Escolhi abrir o Word')
elif opcao == 'Notepad':
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('notepad')
    escolha_opcao.press('Enter')
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('Escolhi abrir o Notepad')


from selenium import webdriver

abrirNavegador = webdriver.Chrome()
abrirNavegador.get("https://www.google.com.br/")


"""
Extraindo Dólar e Euro da internet
"""
from selenium import webdriver as opcoes_selenium
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoPausaComputador
import pyautogui as teclasAtalhos
import xlsxwriter
import os

from selenium.webdriver.common.by import By

meuNavegador = opcoes_selenium.Chrome()
meuNavegador.get("https://www.google.com.br/")
tempoPausaComputador.sleep(2)

meuNavegador.find_element(By.NAME, "q").send_keys("Dolar hoje")
tempoPausaComputador.sleep(2)

meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)
tempoPausaComputador.sleep(4)

valorDolar = meuNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
print(valorDolar)

tempoPausaComputador.sleep(2)

meuNavegador.find_element(By.NAME, "q").send_keys("")
tempoPausaComputador.sleep(2)

teclasAtalhos.press('tab')

tempoPausaComputador.sleep(4)

teclasAtalhos.press('enter')

tempoPausaComputador.sleep(2)

meuNavegador.find_element(By.NAME, "q").send_keys("Euro hoje")
tempoPausaComputador.sleep(2)

meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)
tempoPausaComputador.sleep(4)

valorEuro = meuNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
print(valorEuro)

tempoPausaComputador.sleep(6)

caminhoArquivo = "/GitHub/RPA/dolar_e_euro.xlsx"
planilhaCriada = xlsxwriter.Workbook(caminhoArquivo)
sheet1 = planilhaCriada.add_worksheet()

sheet1.write("A1", "Dolar")
sheet1.write("B1", "Euro")
sheet1.write("A2", valorDolar)
sheet1.write("B2", valorEuro)

planilhaCriada.close()

os.startfile(caminhoArquivo)

"""
Extraindo endereço pelos sites dos correios e salvando no excel
"""
from Aulas.openpyxl import load_workbook
import os

nome_aquivo_cep = "/GitHub/RPA/PesquisaEndereco_2.xlsx"
planilhaDadosEndereco = load_workbook(nome_aquivo_cep)

sheet_selecionada = planilhaDadosEndereco["CEP"]

from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoEspera
from selenium.webdriver.common.by import By

navegador = opcoesSelenium.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")
tempoEspera.sleep(2)

navegador.find_element(By.NAME, "endereco").send_keys("23548057")
tempoEspera.sleep(2)
navegador.find_element(By.NAME, "btn_pesquisar").click()
tempoEspera.sleep(2)

for linha in range(2, len(sheet_selecionada['A']) + 1):
    tempoEspera.sleep(2)
    navegador.find_element(By.ID, "btn_nbusca").click()
    tempoEspera.sleep(2)

    cepPesquisa = sheet_selecionada['A%s' % linha].value
    tempoEspera.sleep(2)
    navegador.find_element(By.NAME, "endereco").send_keys(cepPesquisa)
    tempoEspera.sleep(2)
    navegador.find_element(By.NAME, "btn_pesquisar").click()
    tempoEspera.sleep(2)

    rua = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')[0].text
    print(rua)
    bairro = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')[0].text
    print(bairro)
    cidade = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')[0].text
    print(cidade)
    cep = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')[0].text
    print(cep)


    sheet_Dados = planilhaDadosEndereco["Dados"]
    linhaPlanilha = len(sheet_Dados['A']) + 1
    
    colunaA = "A" + str(linhaPlanilha)
    colunaB = "B" + str(linhaPlanilha)
    colunaC = "C" + str(linhaPlanilha)
    colunaD = "D" + str(linhaPlanilha)

    sheet_Dados[colunaA] = rua
    sheet_Dados[colunaB] = bairro
    sheet_Dados[colunaC] = cidade
    sheet_Dados[colunaD] = cep

planilhaDadosEndereco.save(filename=nome_aquivo_cep)

os.startfile(nome_aquivo_cep)

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

btn_radio = navegadorFormulario.find_element(By.ID, "166517071_1215509813_label")
tempoEspera.sleep(1)
btn_radio.click()

tempoEspera.sleep(1)

enviar = navegadorFormulario.find_element(By.XPATH, '//[@id="patas]/main/article/section/form/div[2]/button')
enviar.click()

tempoEspera.sleep(10)


"""
criando arquivo de excel com python
"""
import xlsxwriter as opcoesDoXlsxWriter
import os

nomeCaminhoArquivo = '/GitHub/RPA/SegundoExemplo.xlsx'
minhaPlanilha = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetDados = minhaPlanilha.add_worksheet("Dados")


corFonte1 = minhaPlanilha.add_format()
corFonte1.set_font_color('blue')
corFundoFonte = minhaPlanilha.add_format({'align':'center',
                                          'font_color':'white',
                                          'bold': True,
                                          'bg_color': 'gray',
                                          'font_size': 14})

sheetDados.write("A1", "Nome", corFundoFonte)
sheetDados.write("B1", "Idade", corFundoFonte)
sheetDados.write("A2", "Amanda", corFonte1)
sheetDados.write("B2", 21, corFonte1)
sheetDados.write("A3", "Allan", corFonte1)
sheetDados.write("B3", 28, corFonte1)

minhaPlanilha.close()

os.startfile(nomeCaminhoArquivo)


import xlsxwriter as opcoesDoXlsxWriter
import os

nomeCaminhoArquivo = '/GitHub/RPA/MergeCells.xlsx'
workbook = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetPadrao = workbook.add_worksheet()

add_merge_celulas = workbook.add_format({
    'bold': True,
    'border': 6,
    'align': 'center',
    'valign': 'vcenter',
    'size': 30,
    'fg_color': 'blue',
    'font_color': 'white',
})

sheetPadrao.merge_range('B3:I5', 'Teste de merge celulas', add_merge_celulas)

workbook.close()

os.startfile(nomeCaminhoArquivo)


"""
criando arquivo de excel com python
"""
import xlsxwriter as opcoesDoXlsxWriter
import os

nomeCaminhoArquivo = 'formulas.xlsx'
minhaPlanilha = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetDados = minhaPlanilha.add_worksheet("Dados")


sheetDados.write("A1", "Numero 1")
sheetDados.write("B1", "Numero 2")
sheetDados.write("C1", "Formula")

sheetDados.write("A2", 10)
sheetDados.write("A3", 6)
sheetDados.write("A4", 8)
sheetDados.write("A5", 6)
sheetDados.write("A8", "Ana")

sheetDados.write("B2", 7)
sheetDados.write("B3", 5)
sheetDados.write("B4", 3)
sheetDados.write("B5", 1)
sheetDados.write("B8", "Paula")

sheetDados.write_formula("C2", "=A2+B2")
sheetDados.wri
sheetDados.write_formula("C4", "=A4*B4")
sheetDados.write_formula("C5", "=A5/B5")
sheetDados.write_formula("C8", '=CONCAT(A8," ",B8)')

sheetDados.set_column('A:C',15)
minhaPlanilha.close()

os.startfile(nomeCaminhoArquivo)


"""
criando arquivo de excel com python
"""
import xlsxwriter as opcoesDoXlsxWriter
import os

nomeCaminhoArquivo = '/RPA/formulas.xlsx'
minhaPlanilha = opcoesDoXlsxWriter.Workbook(nomeCaminhoArquivo)
sheetDados = minhaPlanilha.add_worksheet("Dados")


sheetDados.write("A1", "Numero 1")
sheetDados.write("B1", "Numero 2")
sheetDados.write("C1", "Formula")

sheetDados.write("A2", 10)
sheetDados.write("A3", 6)
sheetDados.write("A4", 8)
sheetDados.write("A5", 6)
sheetDados.write("A8", "Ana")

sheetDados.write("B2", 7)
sheetDados.write("B3", 5)
sheetDados.write("B4", 3)
sheetDados.write("B5", 1)
sheetDados.write("B8", "Paula")

sheetDados.write_formula("C2", "=A2+B2")
sheetDados.write_formula("C3", "=A3-B3")
sheetDados.write_formula("C4", "=A4*B4")
sheetDados.write_formula("C5", "=A5/B5")
sheetDados.write_formula("C8", '=CONCAT(A8," ",B8)')

sheetDados.set_column('A:C',15)
minhaPlanilha.close()

os.startfile(nomeCaminhoArquivo)