import numpy as np
import random
from livelossplot import PlotLosses
import timeit
import psutil
import decimal

N = 32

#verifica conflitos entre rainhas
def conflito(linha1, coluna1, linha2, coluna2):
    return (linha1 == linha2 or  
            coluna1 == coluna2 or  
            linha1 - coluna1 == linha2 - coluna2 or  
            linha1 + coluna1 == linha2 + coluna2)  

#verifica aptidão para contar os conflitos
def aptidao(node):
    num_conflictos = 0
    for (r1, c1) in enumerate(node):
        for (r2, c2) in enumerate(node):
            if (r1, c1) != (r2, c2):
                num_conflictos += conflito(r1, c1, r2, c2)
    return num_conflictos

#algoritmo de Simulated Annealing
def simulated_annealing(estado, ptemp, temp):
    for i in range(1000):
        temp *= ptemp
        
        if temp == 0 or temp < 0.00001:
            return estado
        
        x = random.randrange(0, nRainhas - 1)
        y = random.randrange(0, nRainhas - 1)
        
        aux = estado.copy()
        aux[y] = x
        
        # Calcula o delta
        delta = aptidao(aux) - aptidao(estado)
        delta = float(delta)
        
        if aptidao(estado) == 0:
            return estado
        
        chance = decimal.Decimal(2.7182) ** (decimal.Decimal(-delta) / decimal.Decimal(temp))
        
        if delta < 0 or random.uniform(0, 1) < chance:
            estado = aux
    
    return estado

nRainhas = N

#Configuração para plotar a perda (loss) durante o treinamento
groups = {'h': ['Aptidao']}
plotlosses = PlotLosses(groups=groups)

init = timeit.default_timer()
ini_mem = psutil.virtual_memory().used >> 20
for i in range(100): 
     
    ind_inicial = np.array([(np.random.randint(nRainhas)) for i in range(nRainhas)]).astype(np.int)
    
    #Aplica o Simulated Annealing
    aux = simulated_annealing(ind_inicial, 0.99, 100)

    #Verifica se a solução é válida
    if(aptidao(aux) == 0):
        print("Melhor resultado obtido: ", aux)
        break
fimit = timeit.default_timer()

#tempo de execução
print("Tempo de execução: ", round((fimit - init), 2), "s")
