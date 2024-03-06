arquivo = open('C:\\Users\\Tecnologia\\Documents\\GitHub\\RPA\\Alunos.txt')
arquivoBlocodeNotas = arquivo.readlines()

nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
faltas = 0

for linha in arquivoBlocodeNotas:
    quebraLinha = linha.split(',')
    linha = [item.split(';', 1)[1] for item in quebraLinha]
    separaLinhaColuna = linha[0].split(';')
    nome = separaLinhaColuna[2]
    print(nome)

    if separaLinhaColuna[3] == "Nota 1":
        print("---------Titulo-----------")
    else:
        nota1 = int(separaLinhaColuna[3])
        nota2 = int(separaLinhaColuna[4])
        nota3 = int(separaLinhaColuna[5])
        nota4 = int(separaLinhaColuna[6])
        faltas = int(separaLinhaColuna[7])

        print("Nota 1:", nota1)
        print("Nota 2:", nota2)
        print("Nota 3:", nota3)
        print("Nota 4:", nota4)
        print("Faltas:", faltas)

        media = (nota1 + nota2 + nota3 + nota4) / 4

        print("Media: ", media)

        if faltas >= 4:
            print("Reprovado(a) por falta")
        else:
            if media >= 6:
                print("Aprovado(a)")
            elif media >= 4:
                print("Recuperacao")
            else: 
                print("Reprovado(a) por media")
        print("-------------------------")


from PyPDF2 import PdfReader

caminhoArquivo = "C:\\Users\\Tecnologia\\Documents\\GitHub\\RPA\\Mercado_Livre.pdf"

arquivo_Mercado_Livre = PdfReader(caminhoArquivo)
numeroPaginas = len(arquivo_Mercado_Livre.pages)

print(f"{numeroPaginas} paginas")

try:
    informacoes = arquivo_Mercado_Livre.metadata
    print(informacoes)
except ArithmeticError:
    print("nao foi possivel acessar as informacoes do documento")




from PyPDF2 import PdfReader
arquivoPDF = PdfReader("C:\\Users\\Tecnologia\\Documents\\GitHub\\RPA\\Evolucao_Amazon.pdf")
contaNumeroPaginas = len(arquivoPDF.pages)

print(contaNumeroPaginas)
pagina = arquivoPDF.pages[0]
textoPagina1 = pagina.extract_text()
print(textoPagina1)



from PyPDF2 import PdfReader

try:
    arquivopdf = PdfReader("Mercado_Livre.pdf")
    dados = arquivopdf.metadata
    num_paginas = len(arquivopdf.pages)
    print("autor:", dados.author if dados.author else "nao disponivel")
    print("criador:", dados.creator if dados.creator else "nao disponivel")
    print("Produtor:", dados.producer if dados.producer else "nao disponivel")
except FileNotFoundError:
    print("Arquivo pdf nao encontrado. veridique o caminho do arquivo")
except Exception as e:
    print(f"Ocorreu um erro: {e}")