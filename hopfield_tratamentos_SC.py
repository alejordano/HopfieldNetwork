#!/usr/bin/python3
# -*- coding: utf-8 -*-

from neupy import algorithms
from neupy import environment
from neupy import plots
from clusters import atratores, atratores_classificacao, dados_localizados, dados_cat
import numpy as np
#from density import param_density
#from go import parametro_go

# vamos começar ligando nossa rede de Hopfield
# ela está no modo sync, que é syncromatic
dhnet = algorithms.DiscreteHopfieldNetwork(mode='sync')
# vamos transformar nossos atratores em vetor
teste = np.array([atratores[2], atratores[0]])  #AQUI TEM QUE MUDAR NO SEGUNDO (1 é tratado, 2 é controle 2 e 0 é controle 1)
# vamos treinar nossa rede de Hopfield
dhnet.train(teste)
#controle_exemplo = atratores[1]


# Vamos fazer o prunning na matrix de pesos
# para garantir que chegue num resultado
#old_weigth = np.array(dhnet.weight, dtype=np.float)/dhnet.weight.max() #??
#new_weigth = np.array(old_weigth)
#new_weigth[abs(new_weigth) <= 0.3] = 0 #SUBSTITUIR PELO NUMERO DO ARTIGO
#dhnet.weight = new_weigth

# vamos ver os genes mais conectados agora
# density = []
# up = [210, 187, 77, 442, 181, 48, 227, 119, 200, 315, 483, 303, 88, 95, 425, 385, 399, 394, 294, 130, 252]
# density = up
lista_nova = [[0, 50],
[1,	210],
[2,	136],
[3,	375],
[4,	130],
[5,	28],
[6,	43],
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


#lista_nova2 = [[14,	6],
[11,	53],
[10, 57],
[7,	61],
[4,	67],
[2,	87],
[25, 156],
[16, 157],
[18, 183],
[21, 184],
[22, 187],
[17, 188],
[15, 190],
[24, 191],
[26, 192],
[20, 199],
[19, 200],
[1,	232],
[3,	280],
[12, 287],
[8,	339],
[9,	352],
[5,	359],
[13, 365],
[23, 372]

density = sorted(lista_nova)#[[0,x] for x in lista_nova]

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

# vamos por em ordem
#density.sort() #menos conectaddos.
#densityrev = sorted(density, reverse = True) #mais conectados.

#print(densityrev)
paciente_total = 0
# Vamos começar agora com a inibição!!
# Vamos testar várias inibições
# de 1 a 50
rede_inibidos = range(50)
# Sempre salvar a quantidade de cada paciente
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
    # Vamos inibir dos nossos pacientes localizados
    # os que fazem parte de um cluster 
    for paciente_numero in range(len(dados_localizados)):
        # Só vamos testar em pacientes com tratado
        # trocar aqui para 0 para testar controle
        if dados_cat[paciente_numero] in [2,0]: #AQUI TEM QUE MUDAR (1 é tratado, 2 é controle 2 e 0 é controle 1)
            # Um paciente por vez
            paciente = dados_localizados[paciente_numero]
            novo_paciente = np.array(paciente)
            genes_desativados = 0
            # Se vamos testar mais de zero inibições
            # Ao testar só zero pode dar um erro
            # Então separei
            if inibidos != 0:
                # Vamos sempre guardar os genes que foram inibidos
                genes_inibidos = {}
                # Vamos precisar por tentativas, por que
                # muitas vezes existem menos de 10 genes para inibir
                tentativas = 0
                # Só inibe se oo gene no controle exemplo 
                # tiver inibido
                # e o gene no paciente tiver expresso
                # dentro da lista de genes para inibir
                for gene_position in range(len(density)):
                    gene = density[gene_position]
                    # Se tiver inibido no atrator controle...
                    #genes_inibidos[gene[1]] = 0
                    if gene_position < 11:
                        novo_paciente[gene[1]] = 0
                    else:
                       novo_paciente[gene[1]] = 1
                    #if gene_position > inibidos:
                     #   break
                # prevendo esse novo paciente que esta inibido
                # print(len(genes_inibidos.keys()))
                estado = dhnet.energy(novo_paciente)[0]
            else:
                estado = dhnet.energy(novo_paciente)[0]

            # verificando quem ele está mais perto
            # Entre os dois atratores dados
            # soma = 1000000000
            # not_non = True
            # for n in range(len(atratores)):
            #     soma2 = abs(estado - atratores[n]).sum()
                # se as somos dos atratores derem iguais
                # significa que os dois estão equidistantes
                # e pode ser qualquer um deles
            #    if soma2 == soma:
            #        not_non = True
            #    elif soma2 < soma:
            #        soma = soma2
            #        atrator = n
            #        not_non = False
            #    n += 1
            
            # Aqui guardamos e vemos se o paciente 
            # virou tratado ou nao
            #print(estado)
            if estado > -70000:
                pacientes_recuperados += 1
            else:
                pacientes_nao_recuperados += 1

    # Guardamos as listas para cada quantidade de inibição
    pacientes_nao_recuperados_por_genes_inibidos.append(
        pacientes_nao_recuperados)
    pacientes_sem_saber_por_genes_inibidos.append(
        pacientes_sem_saber)
    pacientes_recuperados_por_genes_inibidos.append(
        pacientes_recuperados)

print(pacientes_recuperados_por_genes_inibidos)


# se chamar este arquivo
# faremos o gráfico do resultado de hopfield
if __name__ == "__main__":
    print("Preparando gráfico de Hopfield para plotar")
    # usaremos a biblioteca matplotlib para plotar
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