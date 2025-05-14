import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Tamanho da tela
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de pênaltis")

game = True

font = pygame.font.SysFont(None, 48)
text = font.render('Vamos para os pênaltis!', True, (255, 255, 255))

while game:

    for event in pygame.event.get(): #devolve uma lista de eventos

        if event.type == pygame.QUIT:
            game = False

    window.fill((0, 0, 0))
    window.blit(text,(200, 300))

    pygame.display.update()

pygame.quit()