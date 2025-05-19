import pygame
from config import INIT, QUIT, GAME, GAME_OVER

def tela_inicial(window):
    running = True
    clock = pygame.time.Clock()
    image_menu = pygame.image.load('assets/img/menu_jogo.jpg').convert_alpha()
    image_menu = pygame.transform.scale(image_menu, (800, 600))
    while running:
        clock.tick(60)

        for event in pygame.event.get(): #devolve uma lista de eventos

            if event.type == pygame.QUIT:
                running = False
                estado = QUIT
            
            if event.type == pygame.KEYUP:
                running = False
                estado = GAME

        window.blit(image_menu,(0, 0))

        pygame.display.update()

    return estado