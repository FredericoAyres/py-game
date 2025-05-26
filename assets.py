import pygame

# Carrega e ajusta a imagem de fundo do menu
image_menu = pygame.image.load('assets/img/Menu_DesSoft.png')
image_menu = pygame.transform.scale(image_menu, (800, 600))

# Carrega e ajusta a imagem de fundo da tela de informações
informacoes = pygame.image.load('assets/img/Informações_DesSoft.png')
informacoes = pygame.transform.scale(informacoes, (800, 600))

# Carrega e redimensiona todas as imagens do jogo
image_fundo = pygame.image.load('assets/img/Gol_DesSoft.png')
image_fundo = pygame.transform.scale(image_fundo, (800, 600))
image_goleiro = pygame.image.load('assets/img/Goleiro_DesSoft.png')
image_goleiro = pygame.transform.scale(image_goleiro, (160, 135))
image_goleiro2 = pygame.image.load('assets/img/Goleiro2_DesSoft.png')
image_goleiro2 = pygame.transform.scale(image_goleiro2, (160, 135))
image_jogador = pygame.image.load('assets/img/Jogador_DesSoft.png')
image_jogador = pygame.transform.scale(image_jogador, (180, 160))
image_jogador2 = pygame.image.load('assets/img/Jogador2_DesSoft.png')
image_jogador2 = pygame.transform.scale(image_jogador2, (180, 160))
image_bola = pygame.image.load('assets/img/Bola_DesSoft.png')
image_bola = pygame.transform.scale(image_bola, (50, 50))
image_1 = pygame.image.load('assets/img/1_DesSoft.png')
image_1 = pygame.transform.scale(image_1, (400, 400))
image_2 = pygame.image.load('assets/img/2_DesSoft.png')
image_2 = pygame.transform.scale(image_2, (400, 400))
image_3 = pygame.image.load('assets/img/3_DesSoft.png')
image_3 = pygame.transform.scale(image_3, (400, 400))
image_4 = pygame.image.load('assets/img/4_DesSoft.png')
image_4 = pygame.transform.scale(image_4, (400, 400))
image_5 = pygame.image.load('assets/img/5_DesSoft.png')
image_5 = pygame.transform.scale(image_5, (400, 400))
image_goleiro1_direita = pygame.image.load('assets/img/Goleiro_direita_DesSoft.png')
image_goleiro1_direita = pygame.transform.scale(image_goleiro1_direita, (160, 135))
image_goleiro1_esquerda = pygame.image.load('assets/img/Goleiro_esquerda_DesSoft.png')
image_goleiro1_esquerda = pygame.transform.scale(image_goleiro1_esquerda, (160, 135))
image_goleiro2_direita = pygame.image.load('assets/img/Goleiro2_direita_DesSoft.png')
image_goleiro2_direita = pygame.transform.scale(image_goleiro2_direita, (170, 145))
image_goleiro2_esquerda = pygame.image.load('assets/img/Goleiro2_esquerda_DesSoft.png')
image_goleiro2_esquerda = pygame.transform.scale(image_goleiro2_esquerda, (160, 135))

# Carrega e redimensiona a imagem de fundo da tela de game over
image_game_over = pygame.image.load('assets/img/Game_over.jpg')
image_game_over = pygame.transform.scale(image_game_over, (800, 600))

# Lista com os atalhos das músicas de cada time
musicas = [
    'musicas/corinthians.mp3',
    'musicas/sao_paulo.mp3',
    'musicas/palmeiras.mp3',
    'musicas/santos.mp3',
    'musicas/flamengo.mp3',
    'musicas/fluminense.mp3',
    'musicas/botafogo.mp3',
    'musicas/vasco.mp3'
]

FPS = 60