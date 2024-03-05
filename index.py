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