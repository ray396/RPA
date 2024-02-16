"""
Exercício: Análise de Números 

Objetivo: Desenvolver um programa que solicita ao usuário a entrada de um 
número e, com base nesse número, realiza as seguintes operações:

1 -> mostrar o número informado
2 -> informar se o número é par ou impar
3 -> informar se o número é positivo, negativo ou zero.
4 -> se o número for positivo, calcular e mostrar sua raiz quadrada
"""
num = int(input("Digite um valor: "))

print("\no numero digitado é:", num)

if num % 2 == 0:
  print("\nO número é par")
else:
  print("\nO número é impar")

if num > 0:
  print("\no número é positivo")
if num < 0:
  print("\no número é negativo")
if num == 0:
  print("\no número é zero")

if num > 0:
  print("\na raiz quadrada do número é:", num**(1/2))


"""
Exercício: Operações matemáticas básicas

Objetivo: Desenvolver um programa que solicita ao usuário a entrada de dois 
número e, com base nesse número, realiza as seguintes operações:

1 -> calcular e mostrar a soma dos dois números
2 -> calcular e mostrar a subtração do primeiro número pelo segundo
3 -> calcular e mostrar a multiplicação dos dois números
4 -> calcular e mostrar a divisão do primeiro número pelo segundo 
(se o segundo numero não for zero)
5 -> verificar e informar se algum dos números (ou ambos é zero).
6 -> calcular e mostrar a média dos dois números
7 -> comparar os dois números e informar qual é maior ou se são iguais
"""
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
print(f"\nA soma dos dois numeros é: {num1 + num2}")
print(f"\nA subtração do primeiro numero pelo segundo é: {num1 - num2}")
print(f"\nA multiplicação dos dois numeros é: {num1 * num2}")

if num2 != 0:
  print(f"\nA divisão do primeiro numero pelo segundo é: {num1 / num2}")
else:
  print("\nNão é possível dividir por zero!")

if num1 == 0 or num2 == 0:
  print("\nAlgum dos numeros é zero!")
else:
  print("\nNenhum dos numeros é zero!")

media = (num1 + num2) / 2
print(f"\nA media dos dois numeros é: {media}")

if num1 > num2:
  print(f"O primeiro numero {num1} é maior que o segundo {num2}")
elif num1 < num2:
  print(f"O segundo numero {num2} é maior que o primeiro {num1}")
else:
  print("Os dois numeros são iguais")


"""
Exercício: Análise de Desempenho do Aluno

Objetivo: Desenvolver um programa que avalie o desempenho de um aluno ao longo dos bimestres. Para isso, o programa deve solicitar as quatro notas bimestrais do aluno e, com base nelas, realiza as seguintes ações:

1 -> Calcular e exibir a média das notas
2 -> Determinar e mostrar a maior e a menor nota entre as inseridas
3 -> Com base na média, informar ao usuario se o aluno está aprovado, em recuperação ou reprovado. Considere os seguintes critérios:
-Aprovado: média >= 7
-Recuperação: 5 <= media < 7
-Reprovado: média < 5
4 -> Calcular e mostrar a quantidade de notas que estão acima da média calculada 
"""
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4
print(f"\nA média das notas é: {media:.2f}")

if n1 > n2 and n1 > n3 and n1 > n4:
  print(f"A maior nota é: {n1}")
elif n2 > n1 and n2 > n3 and n2 > n4:
  print(f"A maior nota é: {n2}")
elif n3 > n1 and n3 > n2 and n3 > n4:
  print(f"A maior nota é: {n3}")
else:
  print(f"A maior nota é: {n4}")

if n1 < n2 and n1 < n3 and n1 < n4:
  print(f"A menor nota é: {n1}")
elif n2 < n1 and n2 < n3 and n2 < n4:
  print(f"A menor nota é: {n2}")
elif n3 < n1 and n3 < n2 and n3 < n4:
  print(f"A menor nota é: {n3}")
else:
  print(f"A menor nota é: {n4}")

if media >= 7:
  print(f"Aprovado! nota: {media:.2f}")
elif media >= 5 and media < 7:
  print(f"Recuperação! nota: {media:.2f}")
else:
  print(f"Reprovado! nota: {media:.2f}")

notas_acima_media = 0
if n1 > media:
  notas_acima_media += 1
if n2 > media:
  notas_acima_media += 1
if n3 > media:
  notas_acima_media += 1
if n4 > media:
  notas_acima_media += 1
print(f"A quantidade de notas acima da média é: {notas_acima_media}")