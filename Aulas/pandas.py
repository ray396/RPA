import pandas as opcoesPandas
import numpy as opcoesNumpy

dataFrame_Datas = opcoesPandas.date_range("20221201", periods=31)
dataFrame_Meses = opcoesPandas.date_range("20221201", periods=12, freq="M")

print(dataFrame_Datas)
print(dataFrame_Meses)


import pandas as opcoesPandas
import numpy as opcoesNumpy

numerosAleatorios = opcoesPandas.DataFrame(opcoesNumpy.random.rand(5,1))

print(numerosAleatorios)


import pandas as opcoesPandas
import numpy as opcoesNumpy

notasAlunos_DF = opcoesPandas.DataFrame({
    "Nome": ["Ana", "Pedro", "Joao"],
    "Media": [9, 7, 10]
})

print(notasAlunos_DF)


from IPython.display import display
import pandas as opcoesPandas

notasAluno_DataFrame = opcoesPandas.DataFrame({
    "Nome": ["Ana", "Pedro", "Joao"],
    "Nota 1": [9, 7, 10],
    "Nota 2": [6, 9, 8],
    "Nota 3": [7, 5, 10],
    "Nota 4": [10, 10, 6]
})

display(notasAluno_DataFrame)


from IPython.display import display
import pandas as opcoesPandas

notasAluno_DataFrame = opcoesPandas.DataFrame({
    "Nome": ["Ana", "Pedro", "Joao"],
    "Nota 1": [9, 7, 10],
    "Nota 2": [6, 9, 8],
    "Nota 3": [7, 5, 10],
    "Nota 4": [10, 10, 6]
})

notasAluno_DataFrame["Media"] = (notasAluno_DataFrame["Nota 1"] + notasAluno_DataFrame["Nota 2"] + notasAluno_DataFrame["Nota 3"] + notasAluno_DataFrame["Nota 4"]) / 4



display(notasAluno_DataFrame)


from IPython.display import display
import pandas as opcoesPandas

notasAluno_DataFrame = opcoesPandas.DataFrame({
    "Nome": ["Ana", "Pedro", "Joao"],
    "Nota 1": [9, 7, 10],
    "Nota 2": [6, 9, 8],
    "Nota 3": [7, 5, 10],
    "Nota 4": [10, 10, 6]
})

notasAluno_DataFrame["Media"] = (notasAluno_DataFrame["Nota 1"] + notasAluno_DataFrame["Nota 2"] + notasAluno_DataFrame["Nota 3"] + notasAluno_DataFrame["Nota 4"]) / 4

notasAluno_DataFrame["Faltas"] = 5

display(notasAluno_DataFrame)


from IPython.display import display
import pandas as opcoesPandas

notasAluno_DataFrame = opcoesPandas.DataFrame({
    "Nome": ["Ana", "Pedro", "Joao"],
    "Nota 1": [9, 7, 10],
    "Nota 2": [6, 9, 8],
    "Nota 3": [7, 5, 10],
    "Nota 4": [10, 10, 6]
})

notasAluno_DataFrame["Media"] = (notasAluno_DataFrame["Nota 1"] + notasAluno_DataFrame["Nota 2"] + notasAluno_DataFrame["Nota 3"] + notasAluno_DataFrame["Nota 4"]) / 4
novaColunaFaltas = [2, 5, 3]
notasAluno_DataFrame["Faltas"] = novaColunaFaltas

display(notasAluno_DataFrame)


from IPython.display import display
import pandas as pd 

vendas_DataFrame = pd.read_excel("C:\\Users\\Tecnologia\\Documents\\GitHub\\RPA\\Vendas_Jan.xlsx")

display(vendas_DataFrame)
display(vendas_DataFrame.index)

vendas_Leonardo_Almeida_DF = vendas_DataFrame.loc[vendas_DataFrame["Vendedor"] == "Leonardo Almeida"]

display(vendas_Leonardo_Almeida_DF)


from IPython.display import display
import pandas as pd 

dataFrameDados = pd.read_excel("C:\\Users\\Tecnologia\\Documents\\GitHub\\RPA\\Deletar_Linhas_Colunas.xlsx")

deletandoLinhasEmBranco = dataFrameDados.dropna()

display(deletandoLinhasEmBranco)