#ex 2
nomes = ["Ana", "Bod", "Alice", "Charlie", "Alex", "Tom"]

nomes_a = list(filter(lambda nome: nome[0] == "A", nomes))

print(nomes_a)