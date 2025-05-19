import pygame
from config import INIT, QUIT, GAME, GAME_OVER

def game_over(window):
    running = True
    clock = pygame.time.Clock()
    image_game_over = pygame.image.load('assets/img/Game_over.jpg').convert_alpha()
    image_game_over = pygame.transform.scale(image_game_over, (800, 600))
    while running:
        clock.tick(60)

        for event in pygame.event.get(): #devolve uma lista de eventos

            if event.type == pygame.QUIT:
                running = False
                estado = QUIT
            
            if event.type == pygame.KEYUP:
                running = False
                estado = GAME

        window.blit(image_game_over,(0, 0))

        pygame.display.update()

    estado = GAME_OVER
    
    return estado