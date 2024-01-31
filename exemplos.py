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