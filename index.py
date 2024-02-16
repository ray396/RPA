"""
classes e objetos
"""
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
meu_livro = Livro("1984", "George Orwell", 1949)

print(meu_livro.ano)
