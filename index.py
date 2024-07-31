import pygame
import random
from string import ascii_uppercase
pygame.init()
clock = pygame.time.Clock()
LARGURA, ALTURA = 800, 600
BRANCO = (255, 255, 255)
COR_DA_FONTE = (0, 0, 0)
COR_DESTAQUE = (0, 0 , 255)
COR_FONTE_DESTAQUE = (255, 255, 255)
TAMANHO_DA_GRADE = 10
TAMANHO_DA_FONTE = 36
ESPACEMENTO = 50
FASES = {
    1: ['BOLA', 'CARRO', 'PAZ', 'OLHO', 'ROSA'],
    2: ['BOLACHA', 'CARINHO', 'PALITO', 'OVELHA', 'RAPOSA'],
    3: ['BATATA', 'NUVEM', 'LAMPADA', 'LIMONADA', 'GUARDA'],
    4: ['BOLO', 'MORADIA', 'PIRULITO', 'GASOLINA', 'SAPATO']
}
fase_atual = 1
total_de_frase = len(FASES)
selecao_temporaria = []
tela = pygame.display.set_mode((LARGURA, ALTURA)), pygame.DOUBLEBUF
pygame.display.set_caption('Caça Palavras')
fonte = pygame.font.Font(None, TAMANHO_DA_FONTE)

def gerar_grande_fase_atual():
    return gerar_grande(FASES[fase_atual], TAMANHO_DA_GRADE)

def gerar_grande(palavras, tamanho):
    for palavra in palavras:
        if len(palavra) > tamanho:
            raise  ValueError(f"A palavra '{palavra}' é muito longa para a grade de tamanho '{tamanho}'") 
    grade = []
    for _ in range(tamanho):   
        linha = []
        for _ in range(tamanho):
            linha.append('')
        grade.append(linha)
    for palavra in palavras:
        palavra_colocada = False
        while not palavra_colocada:
            direcao = random.choice[0, 1]
            if direcao == 0:
                passo = random.choice(range(tamanho - len(palavra) + 1))
                linha = random.choice(range(tamanho))
                cabe_na_grade = True
                for l in range(len(palavra)):
                    if grade[linha][passo + l] != ' ':
                        cabe_na_grade = False
                        break
                    if cabe_na_grade:
                        for l in range(len(palavra)):
                            grade[linha][passo + l] = palavra[1]
                        palavra_colocada = True
                else:
                    passo = random.choice(range(tamanho = len(palavra) + 1))
                    coluna = random.choice(range(tamanho))
                    cabe_na_coluna = True
                    for l in range(len(palavra)):
                        if grade[passo + l][coluna] != ' ':
                            cabe_na_coluna = False
                            break 
                        if cabe_na_coluna:
                            for l in range(len(palavra)):
                                grade[passo + l][coluna] = palavra[l]
                            palavra_colocada = True
    for linha in range(tamanho):
        for coluna in range(tamanho):
            if grade[linha][coluna] == ' ':
                grade[linha][coluna] = random.choice(ascii.uppercase)
    return grade