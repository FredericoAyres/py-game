import pygame
from config import INIT, QUIT, GAME, GAME_OVER

def tela_inicial(window):
    running = True
    clock = pygame.time.Clock()
    image_menu = pygame.image.load('assets/img/menu_jogo.jpg').convert_alpha()
    image_menu = pygame.transform.scale(image_menu, (800, 600))

    pygame.mixer.init()

    botoes = []

    # Primeira linha de botões (Corinthians, SPFC, Palmeiras, Santos)
    for i in range(4):
        botao = pygame.Rect(150 + i * 130, 250, 100, 100)
        botoes.append(botao)

    # Segunda linha de botões (Flamengo, Fluminense, Botafogo, Vasco)
    for i in range(4):
        botao = pygame.Rect(150 + i * 130, 370, 100, 100)
        botoes.append(botao)

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

    # dicio = {"nome_time": [musica, rect]}
    dicionario = {}
    for i in range(len(times)):
        dicionario[times[i]] = [musicas[i], botoes[i]]

    while running:
        clock.tick(60)

        for event in pygame.event.get(): #devolve uma lista de eventos

            if event.type == pygame.QUIT:
                running = False
                estado = QUIT
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for time in dicionario:
                    if dicionario[time][1].collidepoint(pos):
                        running = False
                        estado = GAME

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for time in dicionario:
                    if dicionario[time][1].collidepoint(pos):
                        pygame.mixer.music.load(dicionario[time][0])
                        pygame.mixer.music.play(loops=-1)



        window.blit(image_menu,(0, 0))

        pygame.display.update()

    return estado