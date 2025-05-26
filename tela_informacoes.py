# Importa o módulo pygame e os estados do jogo necessários
import pygame
from config import INIT, QUIT
from assets import *

# Função que representa a tela de informações do jogo
def tela_informacoes(window):

    """
    Exibe a tela de informações do jogo e gerencia a interação do usuário.

    Esta função carrega a imagem de fundo da tela de informações e permite ao 
    usuário retornar à tela inicial através do botão "VOLTAR" ou encerrar o 
    jogo fechando a janela.

    Recebe:
        window: A superfície onde a tela de informações será desenhada.

    Retorna:
            O novo estado do jogo, podendo ser:
            - QUIT: se o usuário fechar a janela.
            - INIT: se o usuário clicar no botão "VOLTAR" para retornar à tela inicial.
    """

    running = True
    clock = pygame.time.Clock()

    # Inicializa o mixer de áudio do jogo
    pygame.mixer.init()

    # Define a área do botão "VOLTAR"
    botao_voltar = pygame.Rect(570, 510, 120, 40)  # ajuste conforme o botão na imagem

    # Loop principal da tela de informacoes
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            # Verifica se foi clicado para sair do jogo
            if event.type == pygame.QUIT:
                running = False
                estado = QUIT

            # Verifica se foi clicado algo com o mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # Verifica se clicou no botão "VOLTAR"
                if botao_voltar.collidepoint(pos):
                    running = False
                    estado = INIT  # Volta para a tela inicial

        # Desenha o fundo com as informações
        window.blit(informacoes, (0, 0))
        pygame.display.update()

    return estado