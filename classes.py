import pygame
import random

class Bola(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 375
        self.rect.y = 470
        self.speedx = 0
        self.speedy = 0
        self.direcao = 0

    def update(self):
        if self.direcao == 1:
            self.speedx = -280/60
            self.speedy = -375/60
            if self.rect.x < 95:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        if self.direcao == 2:
            self.speedx = -280/60
            self.speedy = -195/60
            if self.rect.x < 95:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        if self.direcao == 3:
            self.speedx = 0
            self.speedy = -325/60
            if self.rect.y < 145:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        if self.direcao == 4:
            self.speedx = 285/60
            self.speedy = -325/60
            if self.rect.x > 660:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        if self.direcao == 5:
            self.speedx = 285/60
            self.speedy = -195/60
            if self.rect.x > 660:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        self.rect.x += self.speedx
        self.rect.y += self.speedy


class Jogador(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 450
        self.speedx = 0
        self.speedy = 0
        self.direcao = 0

    def update(self):
        if self.direcao in [1, 2, 3, 4, 5]:
            self.speedx = 155/60
            self.speedy = -100/60
            if self.rect.x > 310:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        self.rect.x += self.speedx
        self.rect.y += self.speedy


class Goleiro(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 315
        self.rect.y = 220
        self.speedx = 0
        self.speedy = 0
        self.direcao = 0

    def update(self):
        if self.direcao == 1:
            self.speedx = -205/60
            self.speedy = -35/60
            if self.rect.x < 40:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        if self.direcao == 2:
            self.speedx = -205/60
            self.speedy = 0
            if self.rect.x < 40:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        if self.direcao == 3:
            self.speedx = 0
            self.speedy = -35/60
            if self.rect.y < 125:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        if self.direcao == 4:
            self.speedx = 360/60
            self.speedy = -100/60
            if self.rect.x > 590:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        if self.direcao == 5:
            self.speedx = 360/60
            self.speedy = 0
            if self.rect.x > 590:
                self.speedx = 0
                self.speedy = 0
                self.direcao = 0
        self.rect.x += self.speedx
        self.rect.y += self.speedy