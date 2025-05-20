import pygame
from config import INIT, QUIT, GAME, GAME_OVER

def game_over(window):
    running = True
    clock = pygame.time.Clock()

    image_game_over = pygame.image.load('assets/img/Game_over.jpg').convert_alpha()
    image_game_over = pygame.transform.scale(image_game_over, (800, 600))

    # Define as áreas dos botões manualmente com base na imagem
    botao_sim = pygame.Rect(215, 500, 150, 60)   # x, y, largura, altura
    botao_nao = pygame.Rect(440, 500, 150, 60)

    estado = GAME_OVER

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = QUIT
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_sim.collidepoint(event.pos):
                    estado = INIT
                    running = False

                if botao_nao.collidepoint(event.pos):
                    estado = QUIT
                    running = False

        window.blit(image_game_over, (0, 0))
        pygame.display.update()

    return estado