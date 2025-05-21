import pygame
from config import INIT, QUIT, GAME_OVER

def game_over(window, resultado):
    running = True
    clock = pygame.time.Clock()

    image_game_over = pygame.image.load('assets/img/Game_over.jpg').convert_alpha()
    image_game_over = pygame.transform.scale(image_game_over, (800, 600))

    botao_sim = pygame.Rect(215, 500, 150, 60)   # x, y, largura, altura
    botao_nao = pygame.Rect(440, 500, 150, 60)

    estado = GAME_OVER

    font_resultado = pygame.font.SysFont(None, 60)
    if resultado == "ganhou":
        mensagem = "VOCÊ GANHOU!" 
    else:
        mensagem = "VOCÊ PERDEU!"
    texto = font_resultado.render(mensagem, True, (255, 255, 0))
    rect = texto.get_rect(center=(387, 290))

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
        window.blit(texto, rect)
        pygame.display.update()

    return estado