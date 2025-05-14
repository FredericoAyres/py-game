import pygame
from config import INIT, QUIT, GAME, GAME_OVER

def jogo_rodando(window):
    running = True
    clock = pygame.time.Clock()
    image_fundo = pygame.image.load('assets/img/Gol_DesSoft.png').convert_alpha()
    image_fundo = pygame.transform.scale(image_fundo,(800, 600))
    image_goleiro = pygame.image.load('assets/img/Goleiro_DesSoft.png').convert_alpha()
    image_goleiro = pygame.transform.scale(image_goleiro,(200, 175))
    image_jogador = pygame.image.load('assets/img/Jogador_DesSoft.png').convert_alpha()
    image_jogador = pygame.transform.scale(image_jogador,(180, 160))
    image_bola = pygame.image.load('assets/img/Bola_DesSoft.png').convert_alpha()
    image_bola = pygame.transform.scale(image_bola,(50, 50))

    while running:
        clock.tick(60)

        for event in pygame.event.get(): #devolve uma lista de eventos

            if event.type == pygame.QUIT:
                running = False
                estado = QUIT

        window.blit(image_fundo, (0, 0))
        window.blit(image_goleiro, (300, 180))
        window.blit(image_jogador, (220, 450))
        window.blit(image_bola, (375, 470))


        pygame.display.flip()
        pygame.display.update()

    return estado