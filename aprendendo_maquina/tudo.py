from sklearn.tree import DecisionTreeClassifier

import numpy as np

dados_frutas = np.array([[140, 1], [130, 1], [150, 0], [170, 0]])

rotulos_frutas = np.array([0, 0, 1, 1])

classificador_arvore = DecisionTreeClassifier()

classificador_arvore.fit(dados_frutas, rotulos_frutas)

fruta_nova = np.array([145, 0])

fruta_nova = fruta_nova.reshape(1, -1)

previsao = classificador_arvore.predict(fruta_nova)

mapeamento_classes = {0: 'maca', 1: 'laranja'}

descricao_previsao = mapeamento_classes[previsao[0]]

print(f"A fruta com peso {fruta_nova[0][0]}g e textura {'suave' if fruta_nova[0][1] == 1 else 'aspera'} é provavelmente uma {descricao_previsao}.")

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

palavras = ["maca", "banana", "uva", "cachorro", "gato", "carro"]
rotulos = [1, 1, 1, 0, 0, 0]

modelo = make_pipeline(CountVectorizer(), MultinomialNB())
modelo.fit(palavras, rotulos)

nova_palavra = ["banana"]

previsao = modelo.predict(nova_palavra)

print("previsao:", "fruta" if previsao[0] == 1 else "não é uma fruta")