# Importa módulos necessários e estados do jogo
import pygame
import random
from config import INIT, QUIT, GAME, GAME_OVER
from classes import Bola, Jogador, Goleiro
from assets import *

# Função principal do jogo, onde ocorre a lógica do gameplay
def jogo_rodando(window):

    """
    Executa a lógica principal do jogo de pênaltis.

    Esta função faz toda a dinâmica do jogo, incluindo carregamento de recursos gráficos,
    inicialização dos objetos do jogo (jogador, goleiro, bola), controle de eventos do teclado,
    alternância de turnos entre chute e defesa, atualização de placar, e verificação de condições 
    de vitória ou empate. O jogo inclui uma disputa de pênaltis tradicional e, em caso de empate, 
    uma disputa alternada até definição de vencedor.

    Args:
        window: A superfície onde todos os elementos gráficos do jogo serão desenhados.

    Retorna:
                O estado final do jogo, sendo GAME_OVER ou QUIT.
                O resultado do jogo, podendo ser:
                - "ganhou": se o jogador venceu a disputa.
                - "perdeu": se o jogador perdeu a disputa.
    """

    # Inicia a variável de controle do loop
    running = True
    # Cria um relógio para controlar o fps
    clock = pygame.time.Clock()

    sprites_goleiro1 = {
        1: image_goleiro1_esquerda,
        2: image_goleiro1_esquerda,  
        3: image_goleiro,
        4: image_goleiro1_direita,
        5: image_goleiro1_direita
    }

    sprites_goleiro2 = {
        1: image_goleiro2_esquerda,
        2: image_goleiro2_esquerda,  
        3: image_goleiro2,
        4: image_goleiro2_direita,
        5: image_goleiro2_direita
    }
    # Define as fontes para textos
    font = pygame.font.SysFont(None, 48)
    font_resultado = pygame.font.SysFont(None, 96)

    # Cria instâncias dos personagens e da bola
    goleiro = Goleiro(image_goleiro, sprites_goleiro1)
    jogador = Jogador(image_jogador)
    bola = Bola(image_bola)
    goleiro2 = Goleiro(image_goleiro2, sprites_goleiro2)
    jogador2 = Jogador(image_jogador2)

    # Define quem está jogando no momento
    jogador_atual = jogador
    goleiro_atual = goleiro

    # Placar inicial
    placar_jogador = 0
    placar_cpu = 0

    # Define turno inicial (chute)
    turno = "chute"
    esperando_chute = True

    # Contadores de rodadas
    rodadas_jogador = 0
    rodadas_cpu = 0
    max_rodadas = 5

    # Controle de disputa alternada em caso de empate
    alternadas = False
    rodada_alternada = 0
    alternadas_msg_exibida = False

    # Estado padrão de retorno ao final do jogo
    estado = GAME_OVER

    # Loop principal do jogo
    while running:
        # Controla o fps
        clock.tick(60)

        # Verifica eventos de teclado e janela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                estado = QUIT

            # Aguarda o chute/defesa do jogador
            if esperando_chute and event.type == pygame.KEYUP:
                if turno == "chute" and (rodadas_jogador < max_rodadas or alternadas):
                    # Jogador escolhe onde vai ser o chute
                    jogador_atual = jogador
                    goleiro_atual = goleiro
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                        direcao = int(event.key - pygame.K_0)
                        jogador_atual.direcao = direcao
                        bola.direcao = direcao
                        bola.ultima_direcao = direcao
                        goleiro_atual.direcao = random.randint(1, 5)
                        goleiro_atual.direcao_ultima = goleiro_atual.direcao
                        goleiro_atual.image = sprites_goleiro1[goleiro.direcao]
                        window.blit(goleiro_atual.image, (goleiro_atual.rect.x, goleiro_atual.rect.y))
                        esperando_chute = False

                elif turno == "defesa" and (rodadas_cpu < max_rodadas or alternadas):
                    # Jogador escolhe onde vai defender
                    jogador_atual = jogador2
                    goleiro_atual = goleiro2
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                        direcao = int(event.key - pygame.K_0)
                        goleiro_atual.direcao = direcao
                        goleiro_atual.direcao_ultima = direcao
                        goleiro_atual.image = sprites_goleiro2[goleiro2.direcao]
                        window.blit(goleiro_atual.image, (goleiro_atual.rect.x, goleiro_atual.rect.y))
                        jogador_atual.direcao = 3
                        bola.direcao = random.randint(1, 5)
                        bola.ultima_direcao = bola.direcao
                        esperando_chute = False

        # Atualiza posições dos objetos
        goleiro_atual.update()
        jogador_atual.update()
        bola.update()

        # Quando a animação do chute termina
        if bola.direcao == 0 and jogador_atual.direcao == 0 and goleiro_atual.direcao == 0 and not esperando_chute:
            # Verifica o resultado do chute
            resultado = "GOL!" if bola.ultima_direcao != goleiro_atual.direcao_ultima else "DEFESA!"

            # Atualiza placar de acordo com o resultado
            if resultado == "GOL!":
                if turno == "chute":
                    placar_jogador += 1
                else:
                    placar_cpu += 1

            # Exibe resultado na tela por 2 segundos
            resultado_text = font_resultado.render(resultado, True, (255, 255, 0))
            resultado_rect = resultado_text.get_rect(center=(400, 300))

            # Desenha elementos do jogo na tela
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

            # Alterna turno ou verifica fim do jogo
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

                # Se rodadas acabaram, verifica empate ou vitória
                if rodadas_jogador >= max_rodadas and rodadas_cpu >= max_rodadas:
                    if placar_jogador == placar_cpu:
                        alternadas = True
                        rodada_alternada = 1
                        if not alternadas_msg_exibida:
                            msg = font.render("Empate! Vamos para as alternadas!", True, (255, 255, 0))
                            msg_rect = msg.get_rect(center=(400, 360))
                            window.blit(msg, msg_rect)
                            pygame.display.flip()
                            pygame.time.wait(2000)
                            alternadas_msg_exibida = True
                    else:
                        pygame.time.wait(2000)
                        running = False
            else:
                # Disputa por pênaltis alternadas
                if turno == "chute":
                    turno = "defesa"
                    jogador_atual = jogador2
                    goleiro_atual = goleiro2
                else:
                    if placar_jogador > placar_cpu:
                        pygame.time.wait(2000)
                        running = False
                    elif placar_cpu > placar_jogador:
                        pygame.time.wait(2000)
                        running = False
                    rodada_alternada += 1
                    turno = "chute"
                    jogador_atual = jogador
                    goleiro_atual = goleiro

            # Prepara para próximo chute
            esperando_chute = True
            jogador_atual.rect.x = 220
            jogador_atual.rect.y = 450
            goleiro_atual.rect.x = 315
            goleiro_atual.rect.y = 220
            bola.rect.x = 375
            bola.rect.y = 470

        # Mostra texto de turno atual
        if turno == "chute":
            text = font.render('Sua vez de chutar!', True, (255, 255, 255))
        else:
            text = font.render('Sua vez de defender!', True, (255, 255, 255))

        if goleiro_atual == goleiro and goleiro.direcao == 0 and goleiro.rect.x == 315 and goleiro.rect.y == 220:
            goleiro.image = sprites_goleiro1[3]
        elif goleiro_atual == goleiro2 and goleiro2.direcao == 0 and goleiro2.rect.x == 315 and goleiro2.rect.y == 220:
            goleiro2.image = sprites_goleiro2[3]
        # Redesenha a tela
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

        # Atualiza a tela
        pygame.display.flip()

    # Retorna o resultado final ao final do jogo
    if placar_jogador > placar_cpu:
        return estado, "ganhou"
    else:
        return estado, "perdeu"