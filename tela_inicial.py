# Importa o módulo pygame e as constantes de estado do jogo
import pygame
from config import INIT, QUIT, GAME, GAME_OVER

# Função que representa a tela inicial do jogo
def tela_inicial(window):
    # Variável de controle do loop da tela inicial
    running = True
    # Relógio para controlar a velocidade dos frames
    clock = pygame.time.Clock()
    # Carrega e ajusta a imagem de fundo do menu
    image_menu = pygame.image.load('assets/img/menu_jogo.jpg').convert_alpha()
    image_menu = pygame.transform.scale(image_menu, (800, 600))

    # Inicializa o mixer de áudio do jogo
    pygame.mixer.init()

    # Cria a lista para armazenar os botões dos times
    botoes = []

    # Cria a primeira linha de botões (Corinthians, São Paulo, Palmeiras e Santos)
    for i in range(4):
        botao = pygame.Rect(150 + i * 130, 250, 100, 100)
        botoes.append(botao)

    # Cria a segunda linha de botões (Flamengo, Fluminense, Botafogo e Vasco)
    for i in range(4):
        botao = pygame.Rect(150 + i * 130, 370, 100, 100)
        botoes.append(botao)

    # Lista com os atalhos das músicas de cada time
    musicas = [
        'musicas/corinthians.mp3',
        'musicas/sao_paulo.mp3',
        'musicas/palmeiras.mp3',
        'musicas/santos.mp3',
        'musicas/flamengo.mp3',
        'musicas/fluminense.mp3',
        'musicas/botafogo.mp3',
        'musicas/vasco.mp3'
    ]

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

    # Cria um dicionário que associa cada time à sua música e botão correspondente
    dicionario = {}
    for i in range(len(times)):
        dicionario[times[i]] = [musicas[i], botoes[i]]

    # Loop principal da tela inicial
    while running:
        # Controla o frame rate para 60 FPS
        clock.tick(60)

        # Captura e trata os eventos do pygame
        for event in pygame.event.get():  # devolve uma lista de eventos

            # Se o usuário fechar a janela, encerra a tela inicial
            if event.type == pygame.QUIT:
                running = False
                estado = QUIT
            
            # Se houver clique do mouse, verifica se foi em algum botão de time
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for time in dicionario:
                    if dicionario[time][1].collidepoint(pos):
                        running = False
                        estado = GAME

            # Ao clicar em um botão, carrega e toca a música do time
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for time in dicionario:
                    if dicionario[time][1].collidepoint(pos):
                        pygame.mixer.music.load(dicionario[time][0])
                        pygame.mixer.music.play(loops=-1)

        # Desenha a imagem de fundo na janela
        window.blit(image_menu, (0, 0))

        # Atualiza a tela
        pygame.display.update()

    # Retorna o novo estado do jogo após sair da tela inicial
    return estado