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