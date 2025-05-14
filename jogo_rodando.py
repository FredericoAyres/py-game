import pygame
from config import INIT, QUIT, GAME

def jogo_rodando(window):
    running = True
    clock = pygame.time.Clock()
    image = pygame.image.load('assets/img/Gol_DesSoft.png').convert_alpha()
    image = pygame.transform.scale(image,(800, 600))
    while running:
        clock.tick(60)

        for event in pygame.event.get(): #devolve uma lista de eventos

            if event.type == pygame.QUIT:
                running = False
                estado = QUIT

        window.blit(image, (0, 0))

        pygame.display.flip()
        pygame.display.update()

    return estado