# Importa os módulos necessários
import pygame
from config import INIT, QUIT, GAME, GAME_OVER,TELA_INFORMACOES
from tela_inicial import tela_inicial
from jogo_rodando import jogo_rodando
from game_over import game_over
from tela_informacoes import tela_informacoes

# Inicializa o Pygame
pygame.init()

# Define o tamanho da janela do jogo
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de pênaltis")

# Define a variável de controle do loop principal
game = True

# Define o estado inicial do jogo como INIT
estado = INIT

# Loop principal do jogo que continua até o estado ser QUIT
while estado != QUIT:
    # Se o estado for INIT chama a tela inicial e atualiza o estado
    if estado == INIT:
        estado = tela_inicial(window)
    # Se o estado for GAME executa o jogo e recebe o novo estado e o resultado
    elif estado == GAME:
        estado, resultado = jogo_rodando(window)
    # Se o estado for GAME_OVER exibe a tela de game over com base no resultado
    elif estado == GAME_OVER:
        estado = game_over(window, resultado)
    # Se o estado for TELA_INFORMACOES exibe a tela de informacoes
    elif estado == TELA_INFORMACOES:
        estado = tela_informacoes(window)
    # Caso não seja nenhuma das opções acima encerra o jogo
    else:
        estado = QUIT

# Encerra o jogo
pygame.quit()