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