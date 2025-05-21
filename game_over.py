# Importa o módulo pygame e os estados do jogo necessários
import pygame
from config import INIT, QUIT, GAME_OVER

# Função que exibe a tela de game over
def game_over(window, resultado):
    # Variável de controle do loop da tela
    running = True
    # Relógio para controlar o intervalo entre frames
    clock = pygame.time.Clock()

    # Carrega e redimensiona a imagem de fundo da tela de game over
    image_game_over = pygame.image.load('assets/img/Game_over.jpg').convert_alpha()
    image_game_over = pygame.transform.scale(image_game_over, (800, 600))

    # Cria os botões "Sim" e "Não" para jogar novamente ou sair
    botao_sim = pygame.Rect(215, 500, 150, 60)   # x, y, largura, altura
    botao_nao = pygame.Rect(440, 500, 150, 60)

    # Define o estado inicial da tela como GAME_OVER
    estado = GAME_OVER

    # Define a fonte e a mensagem de resultado (ganhou ou perdeu)
    font_resultado = pygame.font.SysFont(None, 50)
    if resultado == "ganhou":
        mensagem = "VOCÊ GANHOU!" 
    else:
        mensagem = "VOCÊ PERDEU!"
    texto = font_resultado.render(mensagem, True, (255, 255, 0))
    rect = texto.get_rect(center=(380, 290))

    # Toca a música da tela de game over
    pygame.mixer.music.load('musicas/fox_sports.mp3')
    pygame.mixer.music.play(loops=-1)

    # Loop principal da tela de game over
    while running:
        # Limita a execução a 60  fps
        clock.tick(60)

        # Captura e trata os eventos
        for event in pygame.event.get():
            # Fecha a janela se o usuário clicar no botão de fechar
            if event.type == pygame.QUIT:
                estado = QUIT
                running = False

            # Verifica se o usuário clicou em um dos botões
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_sim.collidepoint(event.pos):
                    estado = INIT  # Reinicia o jogo
                    running = False

                if botao_nao.collidepoint(event.pos):
                    estado = QUIT  # Encerra o jogo
                    running = False

        # Desenha a imagem de fundo e a mensagem na tela
        window.blit(image_game_over, (0, 0))
        window.blit(texto, rect)
        # Atualiza a tela
        pygame.display.update()

    # Retorna o próximo estado do jogo
    return estado