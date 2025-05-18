import pygame
import random
from config import INIT, QUIT, GAME, GAME_OVER
from classes import Bola, Jogador, Goleiro

def jogo_rodando(window):
    running = True
    clock = pygame.time.Clock()

    image_fundo = pygame.image.load('assets/img/Gol_DesSoft.png').convert_alpha()
    image_fundo = pygame.transform.scale(image_fundo, (800, 600))
    image_goleiro = pygame.image.load('assets/img/Goleiro_DesSoft.png').convert_alpha()
    image_goleiro = pygame.transform.scale(image_goleiro, (160, 135))
    image_goleiro2 = pygame.image.load('assets/img/Goleiro2_DesSoft.png').convert_alpha()
    image_goleiro2 = pygame.transform.scale(image_goleiro2, (160, 135))
    image_jogador = pygame.image.load('assets/img/Jogador_DesSoft.png').convert_alpha()
    image_jogador = pygame.transform.scale(image_jogador, (180, 160))
    image_jogador2 = pygame.image.load('assets/img/Jogador2_DesSoft.png').convert_alpha()
    image_jogador2 = pygame.transform.scale(image_jogador2, (180, 160))
    image_bola = pygame.image.load('assets/img/Bola_DesSoft.png').convert_alpha()
    image_bola = pygame.transform.scale(image_bola, (50, 50))
    image_1 = pygame.image.load('assets/img/1_DesSoft.png').convert_alpha()
    image_1 = pygame.transform.scale(image_1, (400, 400))
    image_2 = pygame.image.load('assets/img/2_DesSoft.png').convert_alpha()
    image_2 = pygame.transform.scale(image_2, (400, 400))
    image_3 = pygame.image.load('assets/img/3_DesSoft.png').convert_alpha()
    image_3 = pygame.transform.scale(image_3, (400, 400))
    image_4 = pygame.image.load('assets/img/4_DesSoft.png').convert_alpha()
    image_4 = pygame.transform.scale(image_4, (400, 400))
    image_5 = pygame.image.load('assets/img/5_DesSoft.png').convert_alpha()
    image_5 = pygame.transform.scale(image_5, (400, 400))

    font = pygame.font.SysFont(None, 48)
    font_resultado = pygame.font.SysFont(None, 96)

    goleiro = Goleiro(image_goleiro)
    jogador = Jogador(image_jogador)
    bola = Bola(image_bola)
    goleiro2 = Goleiro(image_goleiro2)
    jogador2 = Jogador(image_jogador2)

    jogador_atual = jogador
    goleiro_atual = goleiro

    placar_jogador = 0
    placar_cpu = 0

    turno = "chute"
    esperando_chute = True

    rodadas_jogador = 0
    rodadas_cpu = 0
    max_rodadas = 5

    alternadas = False
    rodada_alternada = 0
    alternadas_msg_exibida = False

    estado = GAME

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                estado = QUIT

            if esperando_chute and event.type == pygame.KEYUP:
                if turno == "chute" and (rodadas_jogador < max_rodadas or alternadas):
                    jogador_atual = jogador
                    goleiro_atual = goleiro
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                        direcao = int(event.key - pygame.K_0)
                        jogador_atual.direcao = direcao
                        bola.direcao = direcao
                        bola.ultima_direcao = direcao
                        goleiro_atual.direcao = random.randint(1, 5)
                        goleiro_atual.direcao_ultima = goleiro_atual.direcao
                        esperando_chute = False

                elif turno == "defesa" and (rodadas_cpu < max_rodadas or alternadas):
                    jogador_atual = jogador2
                    goleiro_atual = goleiro2
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                        direcao = int(event.key - pygame.K_0)
                        goleiro_atual.direcao = direcao
                        goleiro_atual.direcao_ultima = direcao
                        jogador_atual.direcao = 3
                        bola.direcao = random.randint(1, 5)
                        bola.ultima_direcao = bola.direcao
                        esperando_chute = False

        goleiro_atual.update()
        jogador_atual.update()
        bola.update()

        if bola.direcao == 0 and jogador_atual.direcao == 0 and goleiro_atual.direcao == 0 and not esperando_chute:
            resultado = "GOL!" if bola.ultima_direcao != goleiro_atual.direcao_ultima else "DEFESA!"

            if resultado == "GOL!":
                if turno == "chute":
                    placar_jogador += 1
                else:
                    placar_cpu += 1

            resultado_text = font_resultado.render(resultado, True, (255, 255, 0))
            resultado_rect = resultado_text.get_rect(center=(400, 300))

            window.blit(image_fundo, (0, 0))
            window.blit(goleiro_atual.image, (goleiro_atual.rect.x, goleiro_atual.rect.y))
            window.blit(jogador_atual.image, (jogador_atual.rect.x, jogador_atual.rect.y))
            window.blit(bola.image, (bola.rect.x, bola.rect.y))
            window.blit(image_1, (-80, -30))
            window.blit(image_2, (-80, 100))
            window.blit(image_3, (200, -30))
            window.blit(image_4, (480, -30))
            window.blit(image_5, (480, 100))
            placar_texto = font.render(f"Jog: {placar_jogador}  -  {placar_cpu} :CPU", True, (255, 255, 255))
            window.blit(placar_texto, (10, 10))
            window.blit(resultado_text, resultado_rect)
            pygame.display.flip()
            pygame.time.wait(2000)

            if not alternadas:
                if turno == "chute":
                    rodadas_jogador += 1
                    turno = "defesa"
                    jogador_atual = jogador2
                    goleiro_atual = goleiro2
                else:
                    rodadas_cpu += 1
                    turno = "chute"
                    jogador_atual = jogador
                    goleiro_atual = goleiro

                if rodadas_jogador >= max_rodadas and rodadas_cpu >= max_rodadas:
                    if placar_jogador == placar_cpu:
                        alternadas = True
                        rodada_alternada = 1
                        if not alternadas_msg_exibida:
                            msg = font.render("Empate! Vamos para as alternadas!", True, (255, 255, 0))
                            msg_rect = msg.get_rect(center=(400, 360))
                            window.blit(msg, msg_rect)
                            pygame.display.flip()
                            pygame.time.wait(2500)
                            alternadas_msg_exibida = True
                    else:
                        pygame.time.wait(2000)
                        estado = GAME_OVER
                        return estado
            else:
                if turno == "chute":
                    turno = "defesa"
                    jogador_atual = jogador2
                    goleiro_atual = goleiro2
                else:
                    if placar_jogador > placar_cpu:
                        pygame.time.wait(2000)
                        return GAME_OVER
                    elif placar_cpu > placar_jogador:
                        pygame.time.wait(2000)
                        return GAME_OVER
                    rodada_alternada += 1
                    turno = "chute"
                    jogador_atual = jogador
                    goleiro_atual = goleiro

            esperando_chute = True
            jogador_atual.rect.x = 220
            jogador_atual.rect.y = 450
            goleiro_atual.rect.x = 315
            goleiro_atual.rect.y = 220
            bola.rect.x = 375
            bola.rect.y = 470

        if turno == "chute":
            text = font.render('Sua vez de chutar!', True, (255, 255, 255))
        else:
            text = font.render('Sua vez de defender!', True, (255, 255, 255))

        window.blit(image_fundo, (0, 0))
        window.blit(goleiro_atual.image, (goleiro_atual.rect.x, goleiro_atual.rect.y))
        window.blit(jogador_atual.image, (jogador_atual.rect.x, jogador_atual.rect.y))
        window.blit(bola.image, (bola.rect.x, bola.rect.y))
        window.blit(image_1, (-80, -30))
        window.blit(image_2, (-80, 100))
        window.blit(image_3, (200, -30))
        window.blit(image_4, (480, -30))
        window.blit(image_5, (480, 100))

        placar_texto = font.render(f"Jog: {placar_jogador}  -  {placar_cpu} :CPU", True, (255, 255, 255))
        window.blit(placar_texto, (10, 10))
        window.blit(text, (10, 70))

        pygame.display.flip()

    return estado