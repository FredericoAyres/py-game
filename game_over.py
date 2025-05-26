# Importa o módulo pygame e os estados do jogo necessários
import pygame
from config import INIT, QUIT, GAME_OVER
from assets import *

# Função que exibe a tela de game over
def game_over(window, resultado):

    """
    Exibe a tela de game over e gerencia a decisão do jogador de reiniciar ou sair do jogo.

    Esta função carrega a tela de game over, exibe uma mensagem indicando se o jogador ganhou 
    ou perdeu, e apresenta dois botões: "Sim" para reiniciar o jogo e "Não" para encerrar. 
    O usuário pode clicar em uma dessas opções ou fechar a janela para sair.

    Recebe:
        window: A superfície onde a tela de game over será desenhada.
        resultado: Resultado da partida, podendo ser:
            - "ganhou": indica vitória.
            - "perdeu": indica derrota.

    Retorna:
            O próximo estado do jogo, podendo ser:
            - INIT: se o jogador optar por reiniciar o jogo.
            - QUIT: se o jogador decidir encerrar o jogo ou fechar a janela.
    """

    # Variável de controle do loop da tela
    running = True
    # Relógio para controlar o intervalo entre frames
    clock = pygame.time.Clock()

    # Cria os botões "Sim" e "Não" para jogar novamente ou sair
    botao_sim = pygame.Rect(215, 500, 150, 60)   # x, y, largura, altura
    botao_nao = pygame.Rect(440, 500, 150, 60)

    # Define o estado inicial da tela como GAME_OVER
    estado = GAME_OVER

    # Define a fonte e a mensagem de resultado (ganhou ou perdeu)
    font_resultado = pygame.font.SysFont(None, 50)
    if resultado == "ganhou":
        mensagem = "VOCÊ GANHOU!" 
    else:
        mensagem = "VOCÊ PERDEU!"
    texto = font_resultado.render(mensagem, True, (255, 255, 0))
    rect = texto.get_rect(center=(380, 290))

    # Toca a música da tela de game over
    pygame.mixer.music.load('musicas/fox_sports.mp3')
    pygame.mixer.music.play()

    # Loop principal da tela de game over
    while running:
        # Limita a execução a 60  fps
        clock.tick(60)

        # Captura e trata os eventos
        for event in pygame.event.get():
            # Fecha a janela se o usuário clicar no botão de fechar
            if event.type == pygame.QUIT:
                estado = QUIT
                running = False

            # Verifica se o usuário clicou em um dos botões
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_sim.collidepoint(event.pos):
                    estado = INIT  # Reinicia o jogo
                    running = False

                if botao_nao.collidepoint(event.pos):
                    estado = QUIT  # Encerra o jogo
                    running = False

        # Desenha a imagem de fundo e a mensagem na tela
        window.blit(image_game_over, (0, 0))
        window.blit(texto, rect)
        # Atualiza a tela
        pygame.display.update()

    # Retorna o próximo estado do jogo
    return estado