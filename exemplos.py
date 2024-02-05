#for Nested loops -> refere-se à pratica de aninhar um ou mais loops for dentro de outro loop for

#exemplo de loops aninhados
for i in range(1, 4):
    for j in range(1,4):
        print(i, "*",j,"=",i*j)

quadrados_impares = [x**2 for x in range(10) if x % 2 != 0]
print(quadrados_impares)

#outra forma de fazer 
quadrados_impares = []
for x in range(10):
    if x % 2 != 0:
        print(x)
        quadrados_impares.append(x**2)
print(quadrados_impares) 


texto = "Hello World"
consoantes = [char for char in texto if char.lower() not in 'aeiou']
print(consoantes)

#outra forma de fazer
consoantes_dois = []
for letra in texto:
    if letra.lower() not in 'aeiou':
        consoantes_dois.append(letra)
print(consoantes_dois)

"""
Digite um numero inteiro não negativo: 5
O fatorial de 5 é: 120
"""

numero = input("Digite um numero inteiro nao negativo: ")

if numero < 0:
    print("O numero deve ser nao negativo: ")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print("O fatorial de", numero,"e", fatorial)

#for criando um retangulo

largura = 5
altura = 3

for i in range(altura):
    for j in range(largura):
        print("*", end=" ")
    print()

#for criando um triângulo
    
alturadois = 5

for i in range(alturadois):
    espacos = alturadois - i - 1
    asteriscos = 2 * i + 1
    print(" " * espacos + "*" * asteriscos)


# funções 
def soma(a, b):
    return a + b

resultado = soma(2, 3)
print(resultado)

def saudacao(nome):
    print("Olá, " + nome + "! Bem-vindo!")

nome_usuario = "João"
saudacao(nome_usuario)

def exibir_informacoes(nome, idade, cidade="Desconhecida"):
    print("Nome:", nome)
    print("Idade:", idade)
    print("Cidade:", cidade)

exibir_informacoes("Maria", 25, "Manaus")

def soma(*args):
    resultado = sum(args)
    return resultado

total = soma(2, 4, 5, 8, 10, 20)
print(total)

# funções 
def exibir_informacoes(**Kwargs):
    for chave, valor in Kwargs.items():
        print(chave + ": " + str(valor))

exibir_informacoes(nome="Maria", idade=23)

variavel_global = "Eu sou uma variavel global" 
def funcao_exemplo():
    variavel_local = "Eu sou uma variavel local"
    print(variavel_local)
    print(variavel_global) 
funcao_exemplo()

contador = 0
def incrementar_contador():
    global contador
    contador += 1
    print(contador)

incrementar_contador()

def funcao_externa():
    variavel_externa = "Externa"
    def funcao_interna():
        nonlocal variavel_externa
        variavel_externa = "Externa Modificada"
        print(variavel_externa)
    funcao_interna()
    print(variavel_externa)
funcao_externa()

# Exemplo prático: definição e uso

# para dobrar um numero

def dobrar(n):
    return n * 2
print(dobrar(5))

#função Lambda para dobrar um valor
dobrar_lambda = lambda n: n * 2
print(dobrar_lambda(5))

"""
Exemplo de limitações
    expressividade
"""
def classificar_numero(n):
    if n < 0:
        return "negativo"
    elif n == 0:
        return "zero"
    else:
        return "positivo"
print(classificar_numero(5))
classificar_numero_lambda = lambda n: "negativo" if n < 0 else ("zero" if n == 0 else "positivo")
print(classificar_numero_lambda(-5))

#função Lambda com sorted

pessoas = [("Joao", 35), ("bruna", 24), ("carlos",40), ("daniela", 12)]
pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1])

print(pessoas_ordenadas)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_pares = list(filter(lambda x: x % 2 == 0, num))

print(num_pares)

#ex 2
nomes = ["Ana", "Bod", "Alice", "Charlie", "Alex", "Tom"]

nomes_a = list(filter(lambda nome: nome[0] == "A", nomes))

print(nomes_a)


#listas add elementos

#append()
frutas = ["maca", "banana"]
frutas.append("uva")
print(frutas)

#insert()
frutasdois = ["maracuja", "uva", "abacate"]
frutasdois.insert(1, "amora")
print(frutasdois)


#listas remover elementos

#remove()
frutasdois.remove("uva")
print(frutasdois)

#pop()
frutasdois.pop(1)
print(frutasdois)


#listas concatenar listas

# +
num1 = [1, 2, 3]
num2 = [4, 5, 6]

uniao = num1 + num2
print(uniao)

#extend()
num1.extend(num2)
print(num1)


#listas repetir

#*

repeticao = ['a', 'b'] * 3
print(repeticao)

#listas verificar se um item está na lista

print("uva" in frutas)
print('uva' in frutasdois)

"""
Métodos de listas
"""
#sort()
num = [23, 1, 6, 34, 12]
frutas = ['maca', 'uva', 'damasco', 'banana', 'abacaxi']

num.sort()
print(num)
num.sort(reverse=True) #ordenar em ordem decrescente
print(num)

print("\n--------------\n")

frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)


ocorrencias_banana = frutas.count("banana")
print(ocorrencias_banana)

"""
Slicing de listas
"""
minha_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# acessar subconjuntos de listas

subconjuntos = minha_lista[1:4]
print(subconjuntos)

# omissão de indices iniciais ou finais
primeiros_elementos = minha_lista[:2]
print(primeiros_elementos)

# pega todos os elementos a partir do indice 2
elementos_depois_do_indice_2 = minha_lista[2:]
print(elementos_depois_do_indice_2)

# pega todos os elementos com um passo indicado, no exemplo abaixo é 3
elementos_alternados = minha_lista[::3]
print(elementos_alternados)

"""
List Comprehensions
"""
# Exemplo básico

quadrados = [x**2 for x in range(10)]
print(quadrados)

quadrados = []

for x in range(10):
    quadrados.append(x**2)
print(quadrados)

"""
List Aninhadas
"""
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

elemento = matriz[1][1]
print(elemento)

for linha in matriz:
    for coluna in linha:
        print(coluna, end=' ')
    print()

transposta = []
for i in range(len(matriz[0])):
    linha_temporaria = []
    for j in range(len(matriz)):
        linha_temporaria.append(matriz[j][i])
    transposta.append(linha_temporaria)

print(transposta)

"""
Funções com Listas
"""
num = [6, 3, 8, 15, 2, 7, 14]
tamanho = len(num)
print(f"O numero de elementos na lista e: {tamanho}")

maior_valor = max(num)
print(f"O maior valor na lista e: {maior_valor}")

menor_valor = min(num)
print(f"O menor valor na lista e: {menor_valor}")

som_total = sum(num)
print(f"A soma dos elementos na lista e: {som_total}")

#exemplo 1
lista = [23, 45, 67, 89, 12, 56, 78, 90, 34, 56]

tamanho_lista = len(lista)
print(tamanho_lista)

maior = max(lista)
menor = min(lista)
soma = sum(lista)
print(f"Maior: {maior} \nMenor: {menor} \nSoma: {soma}")

#exemplo 2

pesos = [58.5, 63.2, 71.3, 69.4, 68.2]

qdt = len(pesos)
soma = sum(pesos)
media = soma/qdt

print(f"A media e: {media:.2f}")

"""
Iteração em Listas
"""
frutas = ['maca', 'banana', 'cereja', 'damasco', 'figo']

for fruta in frutas:
    print(fruta)

for indice, fruta in enumerate(frutas):
    print(f"Fruta no indice {indice} e {fruta}")

nomes = ['Alice', 'Bruno', 'Clara', 'Daniel', 'Eduarda']

for nome in nomes:
    print(nome)

for indice, nome in enumerate(nomes):
    print(f"{indice + 1}: {nome}")

notas = [85, 90, 78, 92, 88]

print( )

for indice, nome in enumerate(nomes):
    print(f"{nome} obteve nota {notas[indice]}")

"""
Listas e Strings
"""
s = 'Ola'
lista_s = list(s)

print(lista_s)

frase = 'Python e divertido'
palavras = frase.split()
print(palavras)

data = '26/06/2000'
elementos_data = data.split("/")
print(elementos_data)

lista_palavras = ['Python', 'e', 'incrivel']
frase_juntada = ' '.join(lista_palavras)
print(frase_juntada)

"""
Acesso aos Elementos
"""

contato = ('Joao Silva', '123-456-7890', 'joao.silva@gmail.com')

nome = contato[0]
print('Nome:', nome)

"""
Imutabilidade
"""

dimensoes_bagagem = (55, 35, 25)

itens_proibidos = ['liquidos acima de 100ml', 'objetos cortantes', 'material explosivo']
regras_bagagem = (dimensoes_bagagem, itens_proibidos)

regras_bagagem[1].append("bateroas de litio")
print(regras_bagagem[1])

"""
Operações com tuplas
"""

#concatenação de tuplas

cidades = (1, 2)
proximas_cidades = (3, 4)

roteiro_viagem = cidades + proximas_cidades
print(roteiro_viagem)

#repetição

cidades_favoritas = (5, 6)
roteiro_rep = cidades_favoritas * 3
print(roteiro_rep)

#verificar se uma cidade está em seu roteiro

roteiro_total = (1, 2, 3, 4, 1, 2, 1, 2)
cidade_inclusa = 2 in roteiro_total
print(cidade_inclusa)

"""
Métodos de tuplas
"""
# count()
vendas = (101, 102, 103, 101, 102, 101, 104)
vendas_produto_101 = vendas.count(101)
print(f"O produto 101 foi vendido {vendas_produto_101} vezes")

# index()
primeiro_dia_venda_103 = vendas.index(103) + 1
print(f"O produto 103 foi vendido pela primeira vez no {primeiro_dia_venda_103} dia da semana")

avaliacoes = (5, 4, 4, 3, 5, 2, 4, 3, 5, 5, 1, 4, 3, 5, 2)

# avaliações de 5 estrelas
numero_de_cinco_estrelas = avaliacoes.count(5)
print(f"O filme recebeu {numero_de_cinco_estrelas} avaliacoes de 5 estrelas")

# qual é a posição da primeira avaliação de 1 estrela?
posicao_uma_estrela = avaliacoes.index(1) + 1
print(f"A primeira avaliacao de 1 estrela esta na {posicao_uma_estrela} posicao")

"""
Desempacotamento de tuplas
"""
estudante_info = ("Joao", 20, 85.5)

#desempacotamento

nome, idade, nota = estudante_info

print(f"Nome do estudante: {nome}")
print(f"Idade: {idade}")
print(f"Nota Media: {nota}")

"""
Aplicações Práticas
"""
# retornando múltiplos valores de uma função usando tuplas

def analisar_vendas(vendas_A, vendas_B):
    total_vendido = vendas_A + vendas_B
    mais_vendido = "A" if vendas_A > vendas_B else "B"
    return total_vendido, mais_vendido

total, top_produto = analisar_vendas(100, 85)
print(f"total vendido: {total}")
print(f"produto mais vendido: {top_produto}")
print()

# uso de tuplas em loops for

vendas = [(100, 90), (100, 115), (105, 100)]
for vendas_A, vendas_B in vendas:
    print(f"vendas a: {vendas_A}, vendas de b: {vendas_B}")
print()

"""
Comparando Tuplas
"""
# comparando o primeiro elemento
t1 = (1, 2)
t2 = (1, 3)
print(t1 < t2)

# ignorando elementos iguais
t3 = (1, 2, 3)
t4 = (1, 2, 4)
print(t3 < t4)

# comparando tuplas de diferentes tamanhos 
t1 = (1, 2)
t2 = (1, 2, 3)
print(t1 < t2 )

# comparação de elementos de diferentes tipos:
t1 = (1, "apple")
t2 = (2, "banana")
print(t1 < t2)

# exemplo
t1 = (3, 5)
t2 = (3, 4, 10)
t3 = (3, 6)
t4 = (2, 100)
t5 = (3, 5)

# qual é maior: t1 ou t2?
if t1 > t2:
    r1 = "t1"
else: 
    r1 = "t2"
print(f"{r1} e maior")

print()

# t3 é maior que t1?
if t3 > t1:
    r1 = "t3"
else:
    r1 = "t1"
print(f"{r1} e maior")

print()

# compare t4 e t1. Qual é menor?
if t4 < t1:
    r1 = "t4"
else: 
    r1 = "t1"
print(f"{r1} e menor")

print()

# t1 e t5 são iguais?
print(t1 == t5)

"""
Dicionário
"""
livros = {
    "titulo": "Orgulho e Preconceito",
    "autor": "Jane Austen",
    "ano": 1813
}
print(livros["titulo"])
print(livros)

familia = {
    "pai": {
        "nome": "Roberto",
        "idade": 50
    },
    "mae": {
        "nome": "Clara",
        "idade": 48
    },
    "filho": {
        "nome": "Pedro",
        "idade": 22
    }
}

print(familia["filho"])

"""
Acessando itens do Dicionário
"""
#acessando valores usando chaves

smartphone = {
    "marca": "Apple",
    "modelo": "iPhone 12",
    "cor": "Azul",
    "capacidade": "128GB",
    "sistema": "iOS"
}
print("metodo direto:")
print("Marca:", smartphone["marca"])

print("\nmetodo get:")
print("Modelo:", smartphone.get("modelo"))

# verificando a existência de uma chave

print("\nVerificando a existencia de uma chave")

if "sistema" in smartphone:
    print("O smartphone roda no sistema:", smartphone["sistema"])
else:
    print("Sistema operacional não especificado")

"""
Operações Básicas com Dicionário
"""
produto = {
    "id": 12345,
    "nome": "camisa polo",
    "cor": " vermelho",
    "preco": 49.90,
    "estoque": 100
}

# adicionando itens
produto["marca"] = "FashionBrand"
produto["desconto"] = 10

print("Apos adicionar itens:", produto)

# atualizando itens
produto["preco"] = 59.90
produto["desconto"] = 15

print("\nApos atualizar itens:", produto)

# removendo itens
del produto["desconto"] #remove o item desconto
cor_removida = produto.pop("cor")
print(f"\ncor removida: {cor_removida}")
print("\nApos atualizar deletar itens:", produto)

"""
Métodos de Dicionário
"""
livro = {
    "titulo": "O pequeno principe",
    "autor": "Antoine de Saint-Exupery",
    "ano": 1943,
    "editora": "Reynal & Hitchcock",
    "preco": 20.5
}

# keys(), values() e items()
print("Chaves do dicionario:", list(livro.keys()))
print("Valores do dicionario:", list(livro.values()))
print("Itens do dicionario:", list(livro.items()))

# clear()
copia_livro = livro.copy()
copia_livro.clear() #remove todos os itens do dicionario
print("\ndicionario apos clear():", copia_livro)

# setdefault()
isbn = livro.setdefault("ISBN", "978-3-16-148410-0")
print("\nISBN", isbn)
print("Dicionario apos setdefault():", livro)

# update()
atualizacoes = {
    "preco": 18.5,
    "formato": "capa dura"
}
livro.update(atualizacoes)
print("\ndicionario apos update():", livro)

# fromkeys()
chaves = ["Titulo", "Autor", "sinopse"]
novo_livro = dict.fromkeys(chaves, "Desconhecido")
print("\ndicionario criado com fromkeys()", novo_livro)

"""
Iterando sobre Dicionário
"""
notas = {
    "matematica": 8.5,
    "portugues": 9.0,
    "historia": 7.5,
    "geografia": 8.0,
    "quimica": 9.5
}

# interação sobre as chaves do dicionário
print("materias cursadas pelo aluno:")
for materia in notas:
    print(materia)

print("\nmaterias (usando .keys())")
for materia in notas.keys():
    print(materia)

# interando apenas sobre os valores (notas)
print("\nnotas do aluno:")
total = 0
for nota in notas.values():
    print(nota)
    total += nota
media = total / len(notas)
print("\nmedia das notas:", media)

# interando sobre chaves e valores simultaneamente (itens)
print("\nrelatorio de notas:")
for materia, nota in notas.items():
    print(f"{materia}: {nota}")

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

"""
Dicionário Aninhados
"""
alunos = {

    "Joao":{
        "matematica": 8.5,
        "portugues": 9.0,
        "historia": 7.5
    },
    "Maria":{
        "matematica": 9.5,
        "portugues": 8.0,
        "geografia": 8.7
    },
    "Pedro":{
        "matematica": 7.0,
        "portugues": 7.5,
        "historia": 8.0,
        "geografia": 9.0
    }

}

# acessando notas do joao em matematica

nota_joao_mate = alunos["Joao"]["matematica"]
print(f"nota do joao em matematica:", {nota_joao_mate})

# modificando a nota 
alunos["Maria"]["geografia"] = 9.2
print(f"nota atualizada de maria em geografia:", {alunos['Maria']['geografia']})

# adicionando um nota 
alunos["Pedro"]["quimica"] = 8.8
print(f"nota do pedro em quimica:", {alunos['Pedro']['quimica']})