# Esse arquvo é inútil para o jogo portanto não precisa ser comentado
"""
def desenhar_gol_estado(posicoes):
    simbolos = {
        0: None,   # Mostra o número da posição
        1: 'C',
        2: 'G',
        3: 'X'
    }
    mapa = {i: simbolos.get(posicoes.get(i, 0), None) for i in range(1, 6)}
    def get_val(i):
        return mapa[i] if mapa[i] is not None else str(i)
    print("+-------------------------+")
    print(f"|   {get_val(1):^3}   |  {get_val(3):^3}  |  {get_val(4):^3} |")
    print("|---------+-------+------|")
    print(f"|   {get_val(2):^3}   |       |  {get_val(5):^3} |")
    print("+-------------------------+")

def chute(numero):
    dicionario = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    if numero in dicionario:
        dicionario[numero] = 1
    return dicionario

def defesa(numero):
    dicionario = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    if numero in dicionario:
        dicionario[numero] = 2
    return dicionario

def soma_dicionarios(dicionario1, dicionario2):
    dicionario = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for x in dicionario1:
        if x in dicionario:
            dicionario[x] += dicionario1[x]
    for x in dicionario2:
        if x in dicionario:
            dicionario[x] += dicionario2[x]
    return dicionario

def desenhar_gol_estado_3(posicoes):
    simbolos = {
        1: 'C',
        2: 'G',
        3: 'X'
    }
    def get_val(i):
        valor = posicoes.get(i, 0)
        return simbolos[valor] if valor in simbolos else str(i)
    print("+-------------------------+")
    print(f"|   {get_val(1):^3}   |  {get_val(2):^3}  |  {get_val(3):^3} |")
    print("+-------------------------+")

def chute_alternadas(numero):
    dicionario = {1: 0, 2: 0, 3: 0}
    if numero in dicionario:
        dicionario[numero] = 1
    return dicionario

def defesa_alternadas(numero):
    dicionario = {1: 0, 2: 0, 3: 0}
    if numero in dicionario:
        dicionario[numero] = 2
    return dicionario

def soma_dicionarios_alternadas(dicionario1, dicionario2):
    dicionario = {1: 0, 2: 0, 3: 0}
    for x in dicionario1:
        if x in dicionario:
            dicionario[x] += dicionario1[x]
    for x in dicionario2:
        if x in dicionario:
            dicionario[x] += dicionario2[x]
    return dicionario
"""