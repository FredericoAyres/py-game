# Importa o módulo pygame e as constantes de estado do jogo
import pygame
from config import QUIT, GAME, TELA_INFORMACOES
from assets import *

# Função que representa a tela inicial do jogo
def tela_inicial(window):

    """
    Exibe a tela inicial do jogo e gerencia a interação do usuário.

    Esta função carrega a imagem de fundo do menu, inicializa o mixer de áudio e
    cria os botões correspondentes aos times disponíveis. O usuário pode escolher
    um time clicando em um dos escudos, acionando a reprodução da música do time 
    e alterando o estado do jogo para GAME. Também é possível acessar a tela de
    informações ou encerrar o jogo.

    Recebe:
        window: A superfície onde a tela inicial será desenhada.

    Retorna:
            O novo estado do jogo, podendo ser:
            - QUIT: se o usuário fechar a janela.
            - GAME: se o usuário selecionar um time.
            - TELA_INFORMACOES: se o usuário clicar no botão de informações.
    """

    running = True
    clock = pygame.time.Clock()

    # Inicializa o mixer de áudio do jogo
    pygame.mixer.init()

    # Cria a lista para armazenar os botões dos times
    botoes = []
    for i in range(4):  # Primeira linha
        botao = pygame.Rect(150 + i * 130, 250, 100, 100)
        botoes.append(botao)
    for i in range(4):  # Segunda linha
        botao = pygame.Rect(150 + i * 130, 370, 100, 100)
        botoes.append(botao)

    # Lista com os nomes dos times
    times = [
        'corinthians',
        'sao_paulo',
        'palmeiras',
        'santos',
        'flamengo',
        'fluminense',
        'botafogo',
        'vasco'
    ]

    # Dicionário que associa cada time à sua música e botão
    dicionario = {times[i]: [musicas[i], botoes[i]] for i in range(len(times))}

    # Botão da caixa de informações ("INFOS")
    botao_info = pygame.Rect(575, 500, 100, 50)

    # Loop principal da tela inicial
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

                # Verifica se clicou em algum time
                for time in dicionario:
                    if dicionario[time][1].collidepoint(pos):
                        pygame.mixer.music.load(dicionario[time][0])
                        pygame.mixer.music.play(loops=-1)
                        running = False
                        estado = GAME

                # Verifica se clicou no botão de informações
                if botao_info.collidepoint(pos):
                    running = False
                    estado = TELA_INFORMACOES
                    return estado

        # Desenha a imagem de fundo
        window.blit(image_menu, (0, 0))

        # Atualiza a tela
        pygame.display.update()

    # Retorna o novo estado do jogo
    return estado