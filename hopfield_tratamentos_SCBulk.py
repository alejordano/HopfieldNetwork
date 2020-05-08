#!/usr/bin/python3
# -*- coding: utf-8 -*-

from neupy import algorithms
from neupy import environment
from neupy import plots
from clusters import atratores, atratores_classificacao, dados_localizados, dados_cat
import numpy as np


dhnet = algorithms.DiscreteHopfieldNetwork(mode='sync')
teste = np.array([atratores[2]])  #AQUI TEM QUE MUDAR NO SEGUNDO (1 é tratado, 2 é controle 2 e 0 é controle 1)
dhnet.train(teste)
#dhnet.energy(np.array(dados_localizados[77]))


lista_nova = [[3, 50],
[1,	210],
[2,	136],
[4,	375],
[5,	130],
[6,	28],
[7,	221],
[8,	79],
[9,	153],
[10, 307],
[11, 407],
[12, 295],
[13, 61],
[14, 67],
[15, 371],
[16, 321],
[17, 345],
[18, 338],
[19, 280],
[20, 87],
[21, 232]]

#dados_localizados[140] = bulk controle2
#dados localizados[122] = bulk controle1
#dados_localizados[74] = bulk tratado
density = sorted(lista_nova)#[[0,x] for x in lista_nova]

numeroGenes = []
genes_alterados = 0
paciente = dados_localizados[140]
novo_paciente = np.array(paciente)

for gene_position in range(22):
    gene = density[gene_position]
    if gene_position < 10:
        novo_paciente[gene[1]] = 0
    else:
        novo_paciente[gene[1]] = 1
estado = dhnet.energy(novo_paciente)[0]
genes_alterados += 1
numeroGenes.append(genes_alterados)
print(numeroGenes, estado)


