# Importa o módulo pygame e os estados do jogo necessários
import pygame
from config import INIT, QUIT, GAME_OVER, TELA_INFORMACOES

# Função que representa a tela de informações do jogo
def tela_informacoes(window):
    running = True
    clock = pygame.time.Clock()

    # Carrega e ajusta a imagem de fundo da tela
    informacoes = pygame.image.load('assets/img/Informações_DesSoft.png').convert_alpha()
    informacoes = pygame.transform.scale(informacoes, (800, 600))

    # Inicializa o mixer de áudio do jogo
    pygame.mixer.init()

    # Define a área do botão "VOLTAR"
    botao_voltar = pygame.Rect(590, 510, 120, 40)  # ajuste conforme o botão na imagem

    # Loop principal da tela de informacoes
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                estado = QUIT

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