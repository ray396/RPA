"""
Outras Funções e Métodos
"""
frutas = {"maca", "banana", "laranja","uva","manga"}

# len()
numero_de_frutas = len(frutas)
print(f"O conjunto tem {numero_de_frutas} de frutas")

# in
frutas_desejada = "maca"
if frutas_desejada in frutas:
    print(f"{frutas_desejada} está no conjunto de frutas")