import pygame
import sys
from config import INIT, QUIT, GAME, GAME_OVER
from tela_inicial import tela_inicial
from jogo_rodando import jogo_rodando
from game_over import game_over

# Inicializa o Pygame
pygame.init()

# Tamanho da tela
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de pênaltis")

game = True

estado = INIT

while estado != QUIT:
    if estado == INIT:
        estado = tela_inicial(window)
    elif estado == GAME:
        estado, resultado = jogo_rodando(window)
    elif estado == GAME_OVER:
        estado = game_over(window, resultado)
    else:
        estado = QUIT

pygame.quit()