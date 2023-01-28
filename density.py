#!/usr/bin/python3
# -*- coding: utf-8 -*-

from neupy import algorithms
from neupy import environment
from neupy import plots
from clusters import atratores, atratores_classificacao, dados_localizados, dados_cat
import numpy as np
#from parametro_conservador import paramconservador
#from go import parametro_go
from parametro_Interatoma import param_int

# start Hopfield network, sync mode

dhnet = algorithms.DiscreteHopfieldNetwork(mode='sync')
# transform attractors in vectors 
teste = np.array(atratores)
# train Hopfield network
dhnet.train(teste)
controle_exemplo = atratores[1]


# Prunning weight matrix to ensure reaching a result
#old_weigth = np.array(dhnet.weight, dtype=np.float)/dhnet.weight.max() #??
#new_weigth = np.array(old_weigth)
#new_weigth[abs(new_weigth) <= 0.3] = 0 #SUBSTITUIR PELO NUMERO DO ARTIGO
#dhnet.weight = new_weigth

# check genes with high density
density = []
#density = sorted(param_int, reverse = False)
#print(density)
for x in range(len(dhnet.weight)):
    soma = 0
    # para cada coluna
    for y in dhnet.weight[x,:]:
         #soma cada linha daquela coluna
        soma += abs(y)
    # vamos pegar os nós mais conectados
    # e que estão inibidos no controle
    if controle_exemplo[x] == 0:
        # adiciona 2 variáveis
        # a primeira é a densidade
        # a segunda é a posição
        density.append([float(soma)/len(dhnet.weight),x])
    if controle_exemplo[x] == 1:
        density.append([float(soma) / len(dhnet.weight), x])
density.sort()
print(density)
print("Quantidade de genes que podem ser desativados -> {}".format(len(density)))