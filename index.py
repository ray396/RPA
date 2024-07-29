import pygame
import sys
import random
import os

pygame.init()

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

LARGURA_TELA = 600
ALTURA_TELA = 600

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Quebra-Cabeça')

def listar_imagens(pasta):
    extensoes_validas = ['.jpg', '.jpeg', '.png', '.bmp']
    arquivos = os.listdir(pasta)
    imagens_validas = []
    for arquivo in arquivos:
        extensao = os.path.splitext(arquivo)[1]
        if extensao in extensoes_validas:
            caminho_completo = os.path.join(pasta, arquivo)
            imagens_validas.append(caminho_completo)
    return imagens_validas

def desenha_selecao_imagens(imagens):
    for index, caminho_imagem in enumerate(imagens):
        pygame.draw.rect(tela, (200, 200, 200), (50, index * 80 + 50, 500, 60))
        font = pygame.font.Font(None, 36)
        texto = font.render(os.path.basename(caminho_imagem), True, (50, 50, 50))
        tela.blit(texto, (60, index * 80 + 65))

def desenhar_quebra_cabeca():
    for i, peca in enumerate(pecas):
        x = i % 3
        y = i // 3
        tela.blit(peca[2], (x * TAMANHO_BLOCO_LARGURA, y * TAMANHO_BLOCO_ALTURA))

imagens = listar_imagens(r'C:\Users\Dev\Documents\GitHub\RPA\Imagens')

while True:
    escolhendo_imagem = True
    while escolhendo_imagem:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                start_click = pygame.time.get_ticks()
            if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                end_click = pygame.time.get_ticks()
                if end_click - start_click < 500:
                    x, y = pygame.mouse.get_pos()
                    index = (y - 50) // 80
                    if 50 < x < 550 and 50 + index * 80 < y < 110 + index * 80 and index < len(imagens):
                        imagem_escolhida = imagens[index]
                        escolhendo_imagem = False
        tela.fill(BRANCO)
        desenha_selecao_imagens(imagens)
        pygame.display.flip()
    imagem = pygame.image.load(imagem_escolhida).convert()
    imagem = pygame.transform.scale(imagem, (LARGURA_TELA, ALTURA_TELA))
    TAMANHO_BLOCO_LARGURA = LARGURA_TELA // 3
    TAMANHO_BLOCO_ALTURA = ALTURA_TELA // 3
    pecas = []
    ordem_correta = []
    for i in range(3): 
        for j in range(3):  
            peca = imagem.subsurface(pygame.Rect(i * TAMANHO_BLOCO_LARGURA,
                                                 j * TAMANHO_BLOCO_ALTURA, 
                                                 TAMANHO_BLOCO_LARGURA, 
                                                 TAMANHO_BLOCO_ALTURA))
            ordem_correta.append((i, j, peca))
    pecas = ordem_correta.copy()
    random.shuffle(pecas)
    selecionado = None
    jogo_terminado = False
    while not jogo_terminado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                index = x // TAMANHO_BLOCO_LARGURA + (y // TAMANHO_BLOCO_ALTURA) * 3
                selecionado = index
            if evento.type == pygame.MOUSEBUTTONUP:
                if selecionado is not None:
                    x, y = pygame.mouse.get_pos()
                    index = x // TAMANHO_BLOCO_LARGURA + (y // TAMANHO_BLOCO_ALTURA) * 3
                    pecas[selecionado], pecas[index] = pecas[index], pecas[selecionado]
                    selecionado = None
        tela.fill(BRANCO)
        desenhar_quebra_cabeca()
        pygame.display.flip()
        