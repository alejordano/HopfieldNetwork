#!/usr/bin/python3
# -*- coding: utf-8 -*-

from neupy import algorithms
from neupy import environment
from neupy import plots
from clusters import atratores, pacientes, classificacao
import numpy as np

# Start Hopfiled network in sync mode
dhnet = algorithms.DiscreteHopfieldNetwork(mode='sync')
# transform attractors centroids in vectors
teste = np.array(atratores)
print(teste[0])
# training Hopfield
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

pacientesT_errados = [] #tumor patients that converged to the wrong attractors
#atratores[0] = tratado
#atratores[1] = controle
#pacientes % 2 == 1 = tratado
#pacientes % 2 == 0 = controle
#tratado = np.array([pacientes[x] for x in range(len(pacientes)) if x % 2 == 1]).mean(axis=0)
#paciente = amostra

for x in range(len(pacientes)):
    result = dhnet.predict(np.array(pacientes[x]))
    if (result == atratores[0]).all() or (result == atratores[2]).all(): #if the result is a cancer attractor
        if classificacao[x] == 0 or classificacao[x] == 2: #if it is a tumor sample
              pacientes_tumor_correto += 1
        else: #if it is a control sample
              pacientes_tratado_errados += 1
    else:
         if (result == atratores[1]).all(): #if the result is a treated attractor 
            if classificacao[x] == 0 or classificacao[x] == 2: #if it is a tumor sample
                    pacientes_tumor_errados += 1
                    pacientesT_errados.append(x)
            else: #if it is a treated sample
                    pacientes_tratado_correto += 1
         else: #if the sample converged to none of the attractors
            if classificacao[x] == 0 or classificacao[x] == 2: #if it is a tumor sample
                   pacientes_tumor_ns += 1
            else: #if it is a control sample
                    pacientes_tratado_ns += 1

print("São {} pacientes_tumor_correto, {} pacientes_controle_errados, {} pacientes_tumor_errados, {} pacientes_controle_correto, "
      "{} pacientes_tumor_ns, {} pacientes_controle_ns. ".format(pacientes_tumor_correto, pacientes_tratado_errados, pacientes_tumor_errados,
                                                                 pacientes_tratado_correto, pacientes_tumor_ns, pacientes_tratado_ns))

print("Os pacientes tumorais {} convergiram para o atrator controle.".format(pacientesT_errados))

