# Esse arquvo é inútil para o jogo portanto não precisa ser comentado
"""
from funcoes import desenhar_gol_estado, chute, defesa, soma_dicionarios, desenhar_gol_estado_3, chute_alternadas, defesa_alternadas, soma_dicionarios_alternadas
import random

jogar_novamente = 'sim'

while jogar_novamente == 'sim':

    print('Vamos começar!')
    input()

    placar = {'Jogador': 0, 'Computador': 0}
    
    
    for i in range(5):

        dicionario = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        desenhar_gol_estado(dicionario)
        print('Aonde você deseja chutar?')
        numero = input()
        print('')
        while numero not in [1, 2, 3, 4, 5]:
            if numero in ['1', '2', '3', '4', '5']:
                numero = int(numero)
            else:
                print('Escolha uma posição dentro do gol:')
                numero = input()
                print('')

        dicionario1 = chute(numero)
        
        numero = random.randint(1, 5)
        dicionario2 = defesa(numero)

        dicionario = soma_dicionarios(dicionario1, dicionario2)

        desenhar_gol_estado(dicionario)
        lista = []
        for x in dicionario:
            if dicionario[x] == 3:
                lista.append(dicionario[x])
        if 3 in lista:
            print('O goleiro pegou!')
            input()
        else:
            print('Golaço!')
            input()
            placar['Jogador'] += 1

        
        dicionario = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        desenhar_gol_estado(dicionario)
        print('Aonde você deseja defender?')
        numero = input()
        print('')
        while numero not in [1, 2, 3, 4, 5]:
            if numero in ['1', '2', '3', '4', '5']:
                numero = int(numero)
            else:
                print('Escolha uma posição dentro do gol:')
                numero = input()
                print('')

        dicionario1 = defesa(numero)
        
        numero = random.randint(1, 5)
        dicionario2 = chute(numero)

        dicionario = soma_dicionarios(dicionario1, dicionario2)

        desenhar_gol_estado(dicionario)
        lista = []
        for x in dicionario:
            if dicionario[x] == 3:
                lista.append(dicionario[x])
        if 3 in lista:
            print('Linda defesa!')
            input()
        else:
            print('Quase... Mas não deu para pegar!')
            input()
            placar['Computador'] += 1

        print(f'Placar: {placar}')
        input()

    if placar['Jogador'] > placar['Computador']:
        print('Você ganhou! Parabéns!')
        print('')
    if placar['Jogador'] < placar['Computador']:
        print('Você perdeu! Talvez em uma próxima')
        print('')

    if placar['Jogador'] == placar['Computador']:

        print('Bora para as alternadas! Que vença o melhor!')
        input()

        condicao = True

        while condicao == True:

            dicionario = {1: 0, 2: 0, 3: 0}
            desenhar_gol_estado_3(dicionario)
            print('Aonde você deseja chutar?')
            numero = input()
            print('')
            while numero not in [1, 2, 3]:
                if numero in ['1', '2', '3']:
                    numero = int(numero)
                else:
                    print('Escolha uma posição dentro do gol:')
                    numero = input()
                    print('')

            dicionario1 = chute_alternadas(numero)
            
            numero = random.randint(1, 3)
            dicionario2 = defesa_alternadas(numero)

            dicionario = soma_dicionarios_alternadas(dicionario1, dicionario2)

            desenhar_gol_estado_3(dicionario)
            lista = []
            for x in dicionario:
                if dicionario[x] == 3:
                    lista.append(dicionario[x])
            if 3 in lista:
                print('O goleiro pegou!')
                input()
            else:
                print('Golaço!')
                input()
                placar['Jogador'] += 1

            
            dicionario = {1: 0, 2: 0, 3: 0}
            desenhar_gol_estado_3(dicionario)
            print('Aonde você deseja defender?')
            numero = input()
            print('')
            while numero not in [1, 2, 3]:
                if numero in ['1', '2', '3']:
                    numero = int(numero)
                else:
                    print('Escolha uma posição dentro do gol:')
                    numero = input()
                    print('')

            dicionario1 = defesa_alternadas(numero)
            
            numero = random.randint(1, 3)
            dicionario2 = chute_alternadas(numero)

            dicionario = soma_dicionarios_alternadas(dicionario1, dicionario2)

            desenhar_gol_estado_3(dicionario)
            lista = []
            for x in dicionario:
                if dicionario[x] == 3:
                    lista.append(dicionario[x])
            if 3 in lista:
                print('Linda defesa!')
                input()
            else:
                print('Quase... Mas não deu para pegar!')
                input()
                placar['Computador'] += 1

            print(f'Placar: {placar}')
            input()

            if placar['Jogador'] > placar['Computador']:
                print('Você ganhou! Parabéns!')
                print('')
                condicao = False
            if placar['Jogador'] < placar['Computador']:
                print('Você perdeu! Talvez em uma próxima')
                print('')
                condicao = False
        
    print('Deseja jogar novamente?')
    jogar_novamente = input()

print('O jogo acabou!')
"""