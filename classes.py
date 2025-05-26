# Importa o módulo pygame para recursos gráficos
import pygame
# Importa todos os recursos gráficos e variáveis de assets
from assets import *

# Define a classe Bola, que herda de Sprite
class Bola(pygame.sprite.Sprite):
    # Método construtor da classe Bola
    def __init__(self, img):
        # Inicializa a superclasse Sprite
        pygame.sprite.Sprite.__init__(self)

        # Define a imagem da bola
        self.image = img
        # Obtém o retângulo da imagem para manipular posição
        self.rect = self.image.get_rect()
        # Define posição inicial da bola
        self.rect.x = 375
        self.rect.y = 470
        # Inicializa velocidades
        self.speedx = 0
        self.speedy = 0
        # Direção inicial
        self.direcao = 0

    # Método para atualizar a posição da bola
    def update(self):
        # Direção 1: canto inferior esquerdo
        if self.direcao == 1:
            self.speedx = -280/FPS
            self.speedy = -375/FPS
            # Para o movimento se passar do limite
            if self.rect.x < 95:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        # Direção 2: lado esquerdo
        if self.direcao == 2:
            self.speedx = -280/FPS
            self.speedy = -195/FPS
            if self.rect.x < 95:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        # Direção 3: centro
        if self.direcao == 3:
            self.speedx = 0
            self.speedy = -325/FPS
            if self.rect.y < 145:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        # Direção 4: lado direito
        if self.direcao == 4:
            self.speedx = 285/FPS
            self.speedy = -325/FPS
            if self.rect.x > 660:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        # Direção 5: canto inferior direito
        if self.direcao == 5:
            self.speedx = 285/FPS
            self.speedy = -195/FPS
            if self.rect.x > 660:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        # Atualiza posição da bola
        self.rect.x += self.speedx
        self.rect.y += self.speedy

# Define a classe Jogador, que herda de Sprite
class Jogador(pygame.sprite.Sprite):
    # Método construtor da classe Jogador
    def __init__(self, img):
        # Inicializa a superclasse Sprite
        pygame.sprite.Sprite.__init__(self)

        # Define a imagem do jogador
        self.image = img
        # Obtém o retângulo da imagem para manipular posição
        self.rect = self.image.get_rect()
        # Define posição inicial do jogador
        self.rect.x = 220
        self.rect.y = 450
        # Inicializa velocidades
        self.speedx = 0
        self.speedy = 0
        # Direção inicial
        self.direcao = 0

    # Método para atualizar a posição do jogador
    def update(self):
        # Se direção está entre 1 e 5, o jogador se move
        if self.direcao in [1, 2, 3, 4, 5]:
            self.speedx = 155/FPS
            self.speedy = -100/FPS
            # Para o movimento ao alcançar a posição limite
            if self.rect.x > 310:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        # Atualiza posição do jogador
        self.rect.x += self.speedx
        self.rect.y += self.speedy

# Define a classe Goleiro, que herda de Sprite
class Goleiro(pygame.sprite.Sprite):
    # Método construtor da classe Goleiro
    def __init__(self, img, dic_sprites):
        # Inicializa a superclasse Sprite
        pygame.sprite.Sprite.__init__(self)

        # Define a imagem do goleiro
        self.image = img
        # Obtém o retângulo da imagem para manipular posição
        self.rect = self.image.get_rect()
        # Define posição inicial do goleiro
        self.rect.x = 315
        self.rect.y = 220
        # Inicializa velocidades
        self.speedx = 0
        self.speedy = 0
        # Direção inicial
        self.direcao = 0
        # Dicionário de sprites conforme direção
        self.dic = dic_sprites

    # Método para atualizar a posição do goleiro
    def update(self):
        # Direção 1: pulo para a esquerda e cima
        if self.direcao == 1:
            self.speedx = -205/FPS
            self.speedy = -35/FPS
            self.image = self.dic[1]
            if self.rect.x < 40:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        # Direção 2: pulo lateral para a esquerda
        if self.direcao == 2:
            self.speedx = -205/FPS
            self.speedy = 0
            self.image = self.dic[2]
            if self.rect.x < 40:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        # Direção 3: pulo para cima
        if self.direcao == 3:
            self.speedx = 0
            self.speedy = -35/FPS
            self.image = self.dic[3]
            if self.rect.y < 125:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        # Direção 4: pulo para a direita e cima
        if self.direcao == 4:
            self.speedx = 360/FPS
            self.speedy = -100/FPS
            self.image = self.dic[4]
            if self.rect.x > 590:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        # Direção 5: pulo lateral para a direita
        if self.direcao == 5:
            self.speedx = 360/FPS
            self.speedy = 0
            self.image = self.dic[5]
            if self.rect.x > 590:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        # Atualiza posição do goleiro
        self.rect.x += self.speedx
        self.rect.y += self.speedy