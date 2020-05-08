#!/usr/bin/python3
# -*- coding: utf-8 -*-

from neupy import algorithms
from neupy import environment
from neupy import plots
from clusters import atratores, pacientes, classificacao
import numpy as np

# vamos começar ligando nossa rede de Hopfield
# ela está no modo sync, que é syncromatic
dhnet = algorithms.DiscreteHopfieldNetwork(mode='sync')
# vamos transformar nossos atratores (centroides) em vetor
teste = np.array(atratores)
print(teste[0])
# vamos treinar nossa rede de Hopfield
dhnet.train(teste)
#controle_exemplo = atratores[1]

pacientes_tumor_correto=[]
pacientes_tratado_correto=[]
pacientes_tumor_errados=[]
pacientes_tratado_errados=[]
pacientes_tumor_ns = []
pacientes_tratado_ns = []

pacientes_tumor_correto = 0
pacientes_tratado_correto = 0
pacientes_tumor_errados = 0
pacientes_tratado_errados = 0
pacientes_tumor_ns = 0
pacientes_tratado_ns = 0

pacientesT_errados = [] #pacientes tumorais que convergiram para o atrator errado
#atratores[0] = tratado
#atratores[1] = controle
#pacientes % 2 == 1 = tratado
#pacientes % 2 == 0 = controle
#tratado = np.array([pacientes[x] for x in range(len(pacientes)) if x % 2 == 1]).mean(axis=0)
#paciente = amostra

for x in range(len(pacientes)):
    result = dhnet.predict(np.array(pacientes[x]))
    if (result == atratores[0]).all() or (result == atratores[2]).all(): #se o resultado for o atrator de câncer
        if classificacao[x] == 0 or classificacao[x] == 2: #se a amostra for de câncer
              pacientes_tumor_correto += 1
        else: #se a amostra for normal
              pacientes_tratado_errados += 1
    else:
         if (result == atratores[1]).all(): #se o resultado for o atrator tratado
            if classificacao[x] == 0 or classificacao[x] == 2: #se a amostra for de câncer
                    pacientes_tumor_errados += 1
                    pacientesT_errados.append(x)
            else: #se a amostra for tratada
                    pacientes_tratado_correto += 1
         else: #se o resultado não for nenhum dos dois
            if classificacao[x] == 0 or classificacao[x] == 2: #se a amostra for de câncer
                   pacientes_tumor_ns += 1
            else: #se a amostra for normal
                    pacientes_tratado_ns += 1

print("São {} pacientes_tumor_correto, {} pacientes_controle_errados, {} pacientes_tumor_errados, {} pacientes_controle_correto, "
      "{} pacientes_tumor_ns, {} pacientes_controle_ns. ".format(pacientes_tumor_correto, pacientes_tratado_errados, pacientes_tumor_errados,
                                                                 pacientes_tratado_correto, pacientes_tumor_ns, pacientes_tratado_ns))

print("Os pacientes tumorais {} convergiram para o atrator controle.".format(pacientesT_errados))

