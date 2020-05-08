#!/usr/bin/python3
# -*- coding: utf-8 -*-

from clusters import atratores, atratores_classificacao, dados_localizados
import numpy as np
from scipy.spatial.distance import euclidean

pacientes_Convcontrole = [dados_localizados[i] for i in range(len(dados_localizados)) if i % 2 == 0]
pacientes_Convcontrole.append(dados_localizados[13])
pacientes_Convcontrole.append(dados_localizados[17])
pacientes_Convcontrole.append(dados_localizados[59])
pacientes_Convcontrole.append(dados_localizados[83])
pacientes_Convcontrole.append(dados_localizados[139])

pacientes_Convcancer = [dados_localizados[i] for i in range(len(dados_localizados)) if i % 2 == 1]
del pacientes_Convcancer[6] # número do paciente + 1) /2 = posição. -1 porque começa com 0
del pacientes_Convcancer[7] # -1 a cada um que foi retirado.
del pacientes_Convcancer[26]
del pacientes_Convcancer[38]
del pacientes_Convcancer[65]

print(len(pacientes_Convcontrole), len(pacientes_Convcancer))

distance_controle = 0
total = 0
for paciente in pacientes_Convcontrole:
    for outros in pacientes_Convcontrole:
        distance_controle += euclidean(paciente,outros)
        total += 1

print("Distancia total do controle: {}".format(distance_controle/total))

distance_cancer = 0
total = 0
for paciente in pacientes_Convcancer:
    for outros in pacientes_Convcancer:
        distance_cancer += euclidean(paciente, outros)
        total += 1

print("Distancia total do tratado: {}".format(distance_cancer/total))