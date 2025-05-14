import pygame
from config import INIT, QUIT, GAME, GAME_OVER

def tela_inicial(window):
    running = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)
    text = font.render('Vamos para os pênaltis!', True, (255, 255, 255))
    while running:
        clock.tick(60)

        for event in pygame.event.get(): #devolve uma lista de eventos

            if event.type == pygame.QUIT:
                running = False
                estado = QUIT
            
            if event.type == pygame.KEYUP:
                running = False
                estado = GAME

        window.fill((0, 0, 0))
        window.blit(text,(200, 300))

        pygame.display.flip()
        pygame.display.update()

    return estado