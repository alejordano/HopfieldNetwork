#!/usr/bin/python3
# -*- coding: utf-8 -*-

from neupy import algorithms
from neupy import environment
from neupy import plots
from clusters import atratores, atratores_classificacao, dados_localizados, dados_cat
import numpy as np
from parametro_conservador import paramconservador
#from go import parametro_go
#from parametro_Interatoma import param_int

# Start Hopfiled network in sync mode
dhnet = algorithms.DiscreteHopfieldNetwork(mode='sync')
# transform attractors in vectors
teste = np.array([atratores[1], atratores[0]]) 
# train hopfiled network
dhnet.train(teste)
#controle_exemplo = atratores[1]


# Prunning weight matrix to ensure convergence
#old_weigth = np.array(dhnet.weight, dtype=np.float)/dhnet.weight.max() #??
#new_weigth = np.array(old_weigth)
#new_weigth[abs(new_weigth) <= 0.3] = 0 #SUBSTITUIR PELO NUMERO DO ARTIGO
#dhnet.weight = new_weigth

# most connected
density = []
density = sorted(paramconservador, reverse = False)
print(density)
#for x in range(len(dhnet.weight)):
 #   soma = 0
    # para cada coluna
  #  for y in dhnet.weight[x,:]:
        # soma cada linha daquela coluna
   #     soma += abs(y)
    # vamos pegar os nós mais conectados
    # e que estão inibidos no controle
    #if controle_exemplo[x] == 0:
        # adiciona 2 variáveis
        # a primeira é a densidade 
        # a segunda é a posição
     #   density.append([float(soma)/len(dhnet.weight),x])
#print("Quantidade de genes que podem ser desativados -> {}".format(len(density)))

# by connection order
#density.sort() #menos conectaddos.
#densityrev = sorted(density, reverse = True) #mais conectados.

#print(densityrev)
paciente_total = 0
# Starting multiple inhibitions from 1 to 50
rede_inibidos = range(20)
# saving amount of patients
pacientes_recuperados_por_genes_inibidos = []
pacientes_sem_saber_por_genes_inibidos = []
pacientes_nao_recuperados_por_genes_inibidos = []
# Vamos lá, uma certa quantidade de inibição por vez
for inibidos in rede_inibidos:
    # começa em zero
    pacientes_recuperados = 0
    pacientes_sem_saber = 0
    pacientes_nao_recuperados = 0
    print("Inibidos: {}".format(inibidos))
    # inhibiting samples localised in one of the clusters
    for paciente_numero in range(len(dados_localizados)):
        # Only treated patients; change to 0 to test control 
        if dados_cat[paciente_numero] == 0: #or dados_cat[paciente_numero] == 2:
            # each patient 
            paciente = dados_localizados[paciente_numero]
            energia_inicial = dhnet.energy(np.array(paciente))[0]
            novo_paciente = np.array(paciente)
            genes_desativados = 0
            # if we test more than zero inhibitions: 
            if inibidos != 0:
                # save inhibitied genes
                genes_inibidos = {}
                # Number of tries, we might have less than 10 options
                tentativas = 0
                # Only inhibit if it is inhibitied on the respective control and induced in tumor sample. 
                while ((len(genes_inibidos.keys()) < inibidos) and (tentativas < 100)):
                    tentativas += 1
                    # in each list of genes to inhibit 
                    for gene in density:
                        # if it is inhibited on control attractor
                        if atratores[0][gene[1]] == 0:
                            # if it is expressed on tumor sample 
                            if novo_paciente[gene[1]] == 1:
                                # inhibiting 
                                genes_inibidos[gene[1]] = 0
                                novo_paciente[gene[1]] = 0
                                break
                # checking new patient state 
                # print(len(genes_inibidos.keys()))
                estado = novo_paciente
            else:
                estado = novo_paciente

            energia_final = dhnet.energy(np.array(estado))[0]
            # Verifying if it is closer to one of the attractors 
            if abs(energia_final) - abs(energia_inicial) > 3000:
                pacientes_recuperados += 1
            else:
                pacientes_nao_recuperados += 1
            # save and check sample's state 

    # saving lists to count the number of inhibitions 
    pacientes_nao_recuperados_por_genes_inibidos.append(
        pacientes_nao_recuperados)
    pacientes_sem_saber_por_genes_inibidos.append(
        pacientes_sem_saber)
    pacientes_recuperados_por_genes_inibidos.append(
        pacientes_recuperados)

print(pacientes_recuperados_por_genes_inibidos)

# make Hopfield network graph 
if __name__ == "__main__":
    print("Preparando gráfico de Hopfield para plotar")
    # using matplotlib 
    import matplotlib.pyplot as plt
    import scipy.stats as mlab
    
    plt.figure(figsize=(20,10))
    plt.plot(
        rede_inibidos,
        pacientes_recuperados_por_genes_inibidos,
        linewidth=8.0)
    plt.plot(
        rede_inibidos,
        pacientes_nao_recuperados_por_genes_inibidos,
        linewidth=8.0)
    plt.plot(
        rede_inibidos,
        pacientes_sem_saber_por_genes_inibidos,
        linewidth=8.0)

    plt.xlabel("Number of genes inhibited", fontsize=20)
    plt.ylabel("Quantity of patients", fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=15)
    plt.legend(('Recovered patients',u'Cancer patients', 'Uncertain state'), fontsize = 25)
    plt.show()

    from neupy import plots
    import matplotlib.pyplot as plt

    #plt.figure(figsize=(14, 12))
    #plt.title("Hinton diagram")
    #plots.hinton(new_weigth)
    #plt.show()
