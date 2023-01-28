#!/usr/bin/env python
# -*- coding: utf-8 -*-

# energy graph

# In[95]:


import sklearn.preprocessing
from sklearn.decomposition import PCA
#from clusters import atratores, atratores_classificacao, dados_localizados, dados_cat, classificacao
# from dados_xlsx import new_controle, new_tumor
from scipy.spatial import distance
import numpy as np
from neupy import algorithms

# In[96]:
dhnet = algorithms.DiscreteHopfieldNetwork(mode='sync')
teste = np.array([atratores[0], atratores[1], atratores[2]])  #AQUI TEM QUE MUDAR NO SEGUNDO (1 é tratado, 2 é controle 2 e 0 é controle 1)
dhnet.train(teste)
pca = PCA(n_components=2)


# In[119]:

teste = np.array(list(dados_localizados) + list(atratores), dtype=float)
pca.fit(teste)

energias_teste = []

for y in teste:
    energias_teste.append(dhnet.energy(y)[0])

# In[120]:


print(pca.explained_variance_ratio_)  


# In[121]:


#pca.transform(pacientes[0])


# In[122]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[123]:
def recognize(input_vector):
    soma = 1000000000000000
    print("New input vector")
    m = 0
    vector = np.array(input_vector)
    for y in range(len(teste)):
        soma2 = (abs(teste[y] - vector)).sum()
        if soma2 <= soma: # and soma2 != 0:
            print("{} {}".format(soma2, y))
            soma = soma2
            m = y
    return m

binarizar_inverso = np.vectorize(lambda x: 0 if x < 0.5 else 1)
def energy(input_vector):
    input_vector = binarizar_inverso(input_vector)
    # input_vector = teste[recognize(input_vector)]
    energy = dhnet.energy(input_vector)[0]
    return energy


x = y = np.arange(-8.001, 8.001, 0.5)
X, Y = np.meshgrid(x, y)
energies = map(energy, pca.inverse_transform(list(zip(np.ravel(X), np.ravel(Y)))))
#for data in zip(x,y):
    #energies.append(energy(pca.inverse_transform(data)))

# In[124]:

zs = np.array(list(energies))
Z = zs.reshape(X.shape)
# In[125]:

#pca.transform(pacientes)

# In[138]:

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(121, projection='3d')

correct_ca_y = 0
correct_ca_x = 0
correct_co_y = 0
correct_co_x = 0

pontos = pca.transform(atratores)
for p_n in range(len(atratores)):
    if p_n == 1:
        ax.scatter(pontos[p_n][0] + correct_ca_x, pontos[p_n][1] + correct_ca_y, energy(pca.inverse_transform([[pontos[p_n][0] + correct_ca_x, pontos[p_n][1] + correct_ca_y]])) , s=100, c="red", label="treated")
    elif p_n == 2:
        ax.scatter(pontos[p_n][0] + correct_co_x, pontos[p_n][1] + correct_co_y, energy(pca.inverse_transform([[pontos[p_n][0] + correct_co_x, pontos[p_n][1] + correct_co_y]])), s=100, c="blue", label="control 2")
    else:
        ax.scatter(pontos[p_n][0] + correct_co_x, pontos[p_n][1] + correct_co_y, energy(pca.inverse_transform([[pontos[p_n][0] + correct_co_x, pontos[p_n][1] + correct_co_y]])) , s=100, c="green", label="control 1")

ax.view_init(elev=6, azim=-72)
ax.plot_surface(X, Y, Z, alpha = 0.5)#, cmap='Reds')
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_zlabel('')


ax2 = fig.add_subplot(122)
c = ax2.pcolormesh(X, Y, Z, cmap='RdBu', vmin=Z.min(), vmax=Z.max())

marc1 = 0
marc2 = 0
marc3 = 0

pontos = pca.transform(atratores)
for p_n in range(len(atratores)):
    if p_n == 1:
        marc1 +=1
        if marc1 < 75:
            ax2.scatter(pontos[p_n][0] + correct_ca_x, pontos[p_n][1] + correct_ca_y,
                    s=100, c="red")
        else:
            ax2.scatter(pontos[p_n][0] + correct_ca_x, pontos[p_n][1] + correct_ca_y,
                        s=100, c="yellow", marker='s')
    elif p_n == 2:
        marc2 += 1
        if marc2 < 18:
            ax2.scatter(pontos[p_n][0] + correct_ca_x, pontos[p_n][1] + correct_ca_y,
                    s=100, c="green")
        else:
            ax2.scatter(pontos[p_n][0] + correct_ca_x, pontos[p_n][1] + correct_ca_y,
                        s=100, c="green", marker = 's')
    else:
        marc3 += 1
        if marc3 < 48:
            ax2.scatter(pontos[p_n][0] + correct_co_x, pontos[p_n][1]+ correct_co_y,
                    s=100, c="blue")
        else:
            ax2.scatter(pontos[p_n][0] + correct_co_x, pontos[p_n][1] + correct_co_y,
                        s=100, c="blue", marker = 's')
#plt.imshow(Z, cmap='hot', interpolation='nearest')
ax2.axis([X.min(), X.max(), Y.min(), Y.max()])
fig.colorbar(c)

#plt.show()

# In[146]:

marc1 = 0
marc2 = 0
marc3 = 0

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(121, projection='3d')

pontos = pca.transform(dados_localizados)
for p_n in range(len(dados_localizados)):
    if classificacao[p_n] == 1:
        marc1 += 1
        if marc1 < 75:
            ax.scatter(pontos[p_n][0], pontos[p_n][1], energy(pca.inverse_transform(pontos[p_n])), s=100,
                   c="red", label="Treated")
        else:
            ax.scatter(pontos[p_n][0], pontos[p_n][1], energy(pca.inverse_transform(pontos[p_n])), s=100,
                       c="red", label="", marker = 's')
    elif classificacao[p_n] == 0:
        marc2 += 1
        if marc2 < 48:
            ax.scatter(pontos[p_n][0], pontos[p_n][1], energy(pca.inverse_transform(pontos[p_n])), s=100,
                   c="green", label="Control 1")
        else:
            ax.scatter(pontos[p_n][0], pontos[p_n][1], energy(pca.inverse_transform(pontos[p_n])), s=100,
                       c="green", label="", marker = 's')
    else:
        marc3 += 1
        if marc3 < 18:
            ax.scatter(pontos[p_n][0], pontos[p_n][1], energy(pca.inverse_transform(pontos[p_n])), s=100,
                   c="blue", label="Control 2")
        else:
            ax.scatter(pontos[p_n][0], pontos[p_n][1], energy(pca.inverse_transform(pontos[p_n])), s=100,
                       c="blue", label="", marker = 's')

        
#pontos = pca.transform(atratores)
#for p_n in range(len(atratores)):
 #   if p_n == 1:
  #      ax.scatter(pontos[p_n][0] + correct_ca_x, pontos[p_n][1] + correct_ca_y, energy(pca.inverse_transform([[pontos[p_n][0] + correct_ca_x, pontos[p_n][1] + correct_ca_y]])), s=200, c="purple", label="Treated centroid")
   # elif p_n == 2:
    #    ax.scatter(pontos[p_n][0] + correct_co_x, pontos[p_n][1] + correct_co_y, energy(
     #       pca.inverse_transform([[pontos[p_n][0] + correct_co_x, pontos[p_n][1] + correct_co_y]])) + 1000, s=200,
      #             c="red", label="Control centroid 2")
    #else:
     #   ax.scatter(pontos[p_n][0] + correct_co_x, pontos[p_n][1] +  correct_co_y, energy(pca.inverse_transform([[pontos[p_n][0] + correct_co_x, pontos[p_n][1] + correct_co_y]])), s=200, c="plum", label="Control centroid 1")

ax.view_init(elev=6, azim=-72)
ax.plot_surface(X, Y, Z, alpha = 0.5)#, cmap='Reds')
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_zlabel('')
from collections import OrderedDict
handles, labels = ax.get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), prop={'size': 18})

ax2 = fig.add_subplot(122)
c = ax2.pcolormesh(X, Y, Z, cmap='RdBu', vmin=Z.min(), vmax=Z.max())


marc4 = 0
marc5 = 0
marc6 = 0

pontos = pca.transform(dados_localizados)
for p_n in range(len(dados_localizados)):
    if classificacao[p_n] == 1:
        marc4 += 1
        if marc4 < 75:
            ax2.scatter(pontos[p_n][0], pontos[p_n][1], s=100, c="red")
        else:
            ax2.scatter(pontos[p_n][0], pontos[p_n][1], s=100, c="red", marker = 's')
    elif classificacao[p_n] == 0:
        marc5 += 1
        if marc5 < 48:
            ax2.scatter(pontos[p_n][0], pontos[p_n][1], s=100, c="green")
        else:
            ax2.scatter(pontos[p_n][0], pontos[p_n][1], s=100, c="green", marker = 's')
    elif classificacao[p_n] == 2:
        marc6 += 1
        if marc6 < 18:
            ax2.scatter(pontos[p_n][0], pontos[p_n][1], s=100, c="blue")
        else:
            ax2.scatter(pontos[p_n][0], pontos[p_n][1], s=100, c="blue", marker = 's')
        
#pontos = pca.transform(atratores)
#for p_n in range(len(atratores)):
 #   if p_n == 1:
  #      ax2.scatter(pontos[p_n][0] + correct_ca_x, pontos[p_n][1] + correct_ca_y, 
   #                 s=100, c="purple")
    #elif p_n == 0:
     #   ax2.scatter(pontos[p_n][0] + correct_ca_x, pontos[p_n][1] + correct_ca_y,
         #           s=100, c="plum")
    #else:
     #   ax2.scatter(pontos[p_n][0] + correct_co_x, pontos[p_n][1]+ correct_co_y, 
      #              s=100, c="red")
#plt.imshow(Z, cmap='hot', interpolation='nearest')
ax2.axis([X.min(), X.max(), Y.min(), Y.max()])
fig.colorbar(c)
ax.set_xlabel('', fontsize=18)
ax.set_ylabel('', fontsize=18)
ax.set_zlabel('', fontsize=18)

fig.savefig('myimage.png', format='png', dpi=300)

plt.show()
