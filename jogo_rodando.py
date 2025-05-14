import pygame
import random
from config import INIT, QUIT, GAME, GAME_OVER
from classes import Bola, Jogador, Goleiro

def jogo_rodando(window):
    running = True
    clock = pygame.time.Clock()
    image_fundo = pygame.image.load('assets/img/Gol_DesSoft.png').convert_alpha()
    image_fundo = pygame.transform.scale(image_fundo,(800, 600))
    image_goleiro = pygame.image.load('assets/img/Goleiro_DesSoft.png').convert_alpha()
    image_goleiro = pygame.transform.scale(image_goleiro,(160, 135))
    image_jogador = pygame.image.load('assets/img/Jogador_DesSoft.png').convert_alpha()
    image_jogador = pygame.transform.scale(image_jogador,(180, 160))
    image_bola = pygame.image.load('assets/img/Bola_DesSoft.png').convert_alpha()
    image_bola = pygame.transform.scale(image_bola,(50, 50))
    image_1 = pygame.image.load('assets/img/1_DesSoft.png').convert_alpha()
    image_1 = pygame.transform.scale(image_1,(400, 400))
    image_2 = pygame.image.load('assets/img/2_DesSoft.png').convert_alpha()
    image_2 = pygame.transform.scale(image_2,(400, 400))
    image_3 = pygame.image.load('assets/img/3_DesSoft.png').convert_alpha()
    image_3 = pygame.transform.scale(image_3,(400, 400))
    image_4 = pygame.image.load('assets/img/4_DesSoft.png').convert_alpha()
    image_4 = pygame.transform.scale(image_4,(400, 400))
    image_5 = pygame.image.load('assets/img/5_DesSoft.png').convert_alpha()
    image_5 = pygame.transform.scale(image_5,(400, 400))

    goleiro = Goleiro(image_goleiro)
    jogador = Jogador(image_jogador)
    bola = Bola(image_bola)

    while running:

        clock.tick(60)

        for event in pygame.event.get(): #devolve uma lista de eventos

            if event.type == pygame.QUIT:
                running = False
                estado = QUIT
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    jogador.direcao = 1
                    bola.direcao = 1
                    goleiro.direcao = random.randint(1, 5)
                if event.key == pygame.K_2:
                    jogador.direcao = 2
                    bola.direcao = 2
                    goleiro.direcao = random.randint(1, 5)
                if event.key == pygame.K_3:
                    jogador.direcao = 3
                    bola.direcao = 3
                    goleiro.direcao = random.randint(1, 5)
                if event.key == pygame.K_4:
                    jogador.direcao = 4
                    bola.direcao = 4
                    goleiro.direcao = random.randint(1, 5)
                if event.key == pygame.K_5:
                    jogador.direcao = 5
                    bola.direcao = 5
                    goleiro.direcao = random.randint(1, 5)

        goleiro.update()       
        jogador.update()
        bola.update()

        window.blit(image_fundo, (0, 0))
        window.blit(image_goleiro, (goleiro.rect.x, goleiro.rect.y))
        window.blit(jogador.image, (jogador.rect.x, jogador.rect.y))
        window.blit(bola.image, (bola.rect.x, bola.rect.y))
        window.blit(image_1, (-80, -30))
        window.blit(image_2, (-80, 100))
        window.blit(image_3, (200, -30))
        window.blit(image_4, (480, -30))
        window.blit(image_5, (480, 100))

        pygame.display.flip()
        pygame.display.update()

    return estado