"""
Somar uma coluna
"""
M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Matriz")
for linha in range(4):
    for coluna in range(4):
        print(f"{M[linha][coluna]}", end=" ")
    print()