import numpy as np

import random
from time import perf_counter


N = 32

#Verifica se existe um embate entre duas rainhas nas coordenadas (linha1, coluna1) e (linha2, coluna2).
def conflito(linha1, coluna1, linha2, coluna2):
    return (linha1 == linha2 or  # mesma linha
            coluna1 == coluna2 or  # mesma coluna
            linha1 - coluna1 == linha2 - coluna2 or
            linha1 + coluna1 == linha2 + coluna2)

#Verifica a presença de qualquer conflito na posição (linha, coluna).
def inConflito(estado, linha, coluna):
    return any(conflito(linha, coluna, estado[c], c)
               for c in range(coluna))


#Confere se o estado representa um estado objetivo, livre de conflitos.
def testaObjetivo(estado):
    if estado[-1] == -1:
        return False
    return not any(inConflito(estado, estado[col], col)
                   for col in range(len(state)))

#avaliação heurística, conta o número de conflitos
def heur(node):
    numConflitos = 0
    for (r1, c1) in enumerate(node):
        for (r2, c2) in enumerate(node):
            if (r1, c1) != (r2, c2):
                numConflitos += conflito(r1, c1, r2, c2)
    return -numConflitos

#Encontra o melhor vizinho com a melhor avaliação heurística
def findNeighbor(vizinhos, estado):
    
    vizH = []
    for v in vizinhos:
        vizH.append(heur(v))
    melhores_viz_ind = [i for i, x in enumerate(vizH) if x == max(vizH)]
    melhores_viz = []
    for i in melhores_viz_ind:
        melhores_viz.append(vizinhos[i])
    aux = np.random.randint(0, len(melhores_viz))
    Better = melhores_viz[aux]
    return Better

 #Gera todos os possíveis estados vizinhos
def ProxEstado(N, estado): 
    estados = []
    for linha in range(N):
        for coluna in range(N):
            if coluna != estado[linha]:
                aux = list(estado)
                aux[linha] = coluna
                estados.append(list(aux))
    return estados


def subidaEncosta(N, inicial):
    estado = inicial
    contador = 0
    contador_plato = 0
    log = []
    while True:
        log.append(heur(estado))
        vizinhos = ProxEstado(N, estado)
        if not vizinhos:
            break
        vizinho_selecionado = findNeighbor(vizinhos, inicial)
        if heur(vizinho_selecionado) <= heur(estado):
            break
        else:
            estado = vizinho_selecionado
            contador += 1 
    
    print("Avaliação sobre o resultado: ", -heur(estado))
    print("Número de passos: ", contador)
    return estado, log



def stateRandom(n):
    lista = []
    for i in range(n):
        lista.append(random.randrange(0, n))
    return lista

estado = stateRandom(N)

TimeInitial = perf_counter()

melhorEstado, log = subidaEncosta(N, estado)

print(melhorEstado)
print(f'tempo: {perf_counter() -  TimeInitial}s')
