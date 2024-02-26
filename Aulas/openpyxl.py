"""
openpyxl
"""
from openpyxl import load_workbook
import os 

nome_arquivo = "C:/Users/Tecnologia/Documents/GitHub/RPA/DeletarLinhaColuna.xlsx"
planilha_aberta = load_workbook(filename=nome_arquivo)

sheet_selecionada = planilha_aberta['Aluno']

sheet_selecionada.delete_rows(3)
sheet_selecionada.delete_rows(3)
sheet_selecionada.delete_rows(5)
sheet_selecionada.delete_cols(2)

planilha_aberta.save(filename=nome_arquivo)

os.startfile(nome_arquivo)


"""
openpyxl
"""
from openpyxl import load_workbook
import os 

nome_arquivo = "C:/Users/Tecnologia/Documents/GitHub/RPA/InserirDados.xlsx"
planilha_aberta = load_workbook(filename=nome_arquivo)

sheet_selecionada = planilha_aberta['Aluno']

dadosTabela = [
    ['Nome', 'Idade'],
    ['Benerice', 28],
    ['Caio', 32],
    ['Nicole', 34],
    ['Leonardo', 19],
    ['Amanda', 25]
]
for linhaPlanilha in dadosTabela:
    sheet_selecionada.append(linhaPlanilha)
    
planilha_aberta.save(filename=nome_arquivo)

os.startfile(nome_arquivo)