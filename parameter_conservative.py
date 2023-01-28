#!/usr/bin/python3
# -*- coding: utf-8 -*-

from clusters import pacientes, classificacao, atratores, atratores_classificacao, tratado, controle, controle2
import numpy as np
from scipy.spatial.distance import euclidean

inativos = []
for n in range(len(atratores[0])):
    inativo = 0
    for x in range(len(pacientes)):
        if classificacao[x] == 0: #Needs to change (1 is treated, 2 is control 2 e 0 is control 1)
            if pacientes[x][n] == 1 and atratores[1][n] == 0:
                inativo += 1
    inativos.append([inativo,n])

    inativos.sort()
    #for gene in inativos:
    #    print("Gene na posicao: {} aparece em {} pacientes".format(gene[1], gene[0]))

    paramconservador = []
    paramconservador = sorted(inativos, reverse = False)
    # paramconservador = [[2,152], [2,195]]

    print(paramconservador)