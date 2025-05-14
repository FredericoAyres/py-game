import pygame

# Inicializa o Pygame
pygame.init()

# Tamanho da tela
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de pênaltis")

game = True

while game:

    for event in pygame.event.get(): #devolve uma lista de eventos

        if event.type == pygame.QUIT:
            game = False

    window.fill((0, 0, 0))

    pygame.display.update()

pygame.quit()