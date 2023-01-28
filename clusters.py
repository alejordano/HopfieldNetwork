#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sklearn.preprocessing
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np
from collections import OrderedDict
from pacientes_formula import pacientes_binarizados
from scipy.spatial import distance
from sklearn.manifold import TSNE
import time

pacientes, classificacao = pacientes_binarizados()
dados_localizados = pacientes
dados_cat = classificacao


# treated is categorized as 1
    # control = 0, control 2 = 2.
# median of all treated patients
tratado = np.array([pacientes[x] for x in range(len(pacientes)) if dados_cat[x] == 1]).mean(axis=0)
# median of all control patients
controle = np.array([pacientes[x] for x in range(len(pacientes)) if dados_cat[x] == 0]).mean(axis=0)
controle2 = np.array([pacientes[x] for x in range(len(pacientes)) if dados_cat[x] == 2]).mean(axis=0)

# will have only 2 states; median points from treated and control will be the attractors

atratores_usados = [controle, tratado, controle2]
atratores_classificacao = ["controle", "tratado", "controle"]

# Binarizing median points. The data needs to be binary because of Hopfield 
binarized = []
for atrator in atratores_usados:
    binarized.append([1 if x > 0.5 else 0 for x in atrator])
# saving binarized attractors
atratores = binarized

# PCA
pca = PCA(n_components=2)
pca.fit(pacientes)

print(
        "Explained variance 1st cp: {}; \
    2cp:{}".format(pca.explained_variance_ratio_[0],
                  pca.explained_variance_ratio_[1]))

# if this file exists
# make plot from clusters
if __name__ == "__main__":
    print("Preparando gráfico de clusters para plotar")
    # usaremos a biblioteca matplotlib para plotar
    import matplotlib.pyplot as plt
    import scipy.stats as mlab
    



    
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111)
    #c = ax.pcolormesh(X, Y, Z, cmap='RdBu', vmin=Z.min(), vmax=Z.max())
    print("PRimeiro gráfico, só ver os pontos")
    pontos = pca.transform(pacientes)
    for p_n in range(len(pacientes)):
        ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="purple")
    plt.rcParams['xtick.labelsize'] = 16
    plt.rcParams['ytick.labelsize'] = 16
    #plt.show()
    print("Segundo gráfico")



    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111)
    #c = ax.pcolormesh(X, Y, Z, cmap='RdBu', vmin=Z.min(), vmax=Z.max())

    pontos = pca.transform(pacientes)
    pontinho_c = 0
    pontinho_c1 = 0
    pontinho_t = 0
    pontinho_c2 = 0
    pontinho_c3 = 0
    pontinho_t2 = 0

    for p_n in range(len(pacientes)):
        if dados_cat[p_n] == 1:
                pontinho_t += 1
                if pontinho_t < 75:
                    ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="blue", label="Treated Group")
                else:
                    ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="blue", label="", marker='^')
        elif dados_cat[p_n] == 2:
                pontinho_c1 += 1
                if pontinho_c1 < 18:
                    ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="plum", label="Control 2 Group")
                else:
                    ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="plum", label="", marker='^')
        elif dados_cat[p_n] == 0:
                pontinho_c += 1
                if pontinho_c < 48:
                    ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="red", label="Control 1 Group")
                else:
                    ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="red", label="", marker='^')
    #print("São {} pontos de control e {} pontos de tumor".format(pontinho_c, pontinho_t))
    ax.set_xlabel('1st pc', fontsize=18)
    ax.set_ylabel('2st pc', fontsize=18)
    plt.rcParams['xtick.labelsize'] = 16
    plt.rcParams['ytick.labelsize'] = 16

    from collections import OrderedDict
    handles, labels = ax.get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), prop={'size': 18})
    plt.rcParams['xtick.labelsize'] = 16
    plt.rcParams['ytick.labelsize'] = 16
    plt.show()

    print("Terceiro gráfico")

    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111)
    # c = ax.pcolormesh(X, Y, Z, cmap='RdBu', vmin=Z.min(), vmax=Z.max())

    atratores_usados_pca = pca.transform(atratores)

    pontos = pca.transform(pacientes)
    print(atratores_usados_pca)
    for p_n in range(len(pacientes)):
        if dados_cat[p_n] == 1:
            pontinho_t2 += 1
            if pontinho_t2 < 74:
                ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="blue", label="Treated Group")
            else:
                ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="blue", label="", marker='^')
        elif dados_cat[p_n] == 2:
            pontinho_c2 += 1
            if pontinho_c2 < 18:
                ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="plum", label="Control 2 Group")
            else:
                ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="plum", label="", marker='^')
        elif dados_cat[p_n] == 0:
            pontinho_c3 += 1
            if pontinho_c3 < 48:
                ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="red", label="Control 1 Group")
            else:
                ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="red", label="", marker='^')

    for p_n in range(len(atratores_usados_pca)):
        print(atratores_usados_pca[p_n])
        if p_n == 0:
            ax.scatter(atratores_usados_pca[p_n][0], atratores_usados_pca[p_n][1], s=500, c="black",
                       label="Control 1 centroid")
        elif p_n == 1:
            ax.scatter(atratores_usados_pca[p_n][0], atratores_usados_pca[p_n][1], s=500, c="red",
                       label="Treated centroid")
        else:
            ax.scatter(atratores_usados_pca[p_n][0], atratores_usados_pca[p_n][1], s=500, c="blue",
                       label="Control 2 centroid")

    for i, txt in enumerate(range(len(pacientes))):
        ax.annotate(txt, (pontos[i][0], pontos[i][1]))

    ax.set_xlabel('1st pc', fontsize=20)
    ax.set_ylabel('2st pc', fontsize=20)
    plt.rcParams['xtick.labelsize'] = 16
    plt.rcParams['ytick.labelsize'] = 16

    from collections import OrderedDict
    handles, labels = ax.get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), prop={'size': 22})
    plt.show()

    print("Quarto gráfico TSNE")
    time_start = time.time()
    fashion_tsne = TSNE(random_state=3).fit_transform(pacientes)
    print('t-SNE done! Time elapsed: {} seconds'.format(time.time() - time_start))
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111)
    # c = ax.pcolormesh(X, Y, Z, cmap='RdBu', vmin=Z.min(), vmax=Z.max())

    pontos = fashion_tsne
    pontinho_c = 0
    pontinho_t = 0
    pontinho_c2 = 0
    for p_n in range(len(pacientes)):
        if dados_cat[p_n] == 1:
            pontinho_t += 1
            if pontinho_t < 75:
                ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="blue", label="Treated Group")
            else:
                ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="blue", label="", marker='^')
        elif dados_cat[p_n] == 2:
            pontinho_c += 1
            if pontinho_c < 18:
                ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="plum", label="Control 2 Group")
            else:
                ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="plum", label="", marker='^')
        elif dados_cat[p_n] == 0:
            pontinho_c2 += 1
            if pontinho_c2 < 48:
                ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="red", label="Control 1 Group")
            else:
                ax.scatter(pontos[p_n][0], pontos[p_n][1], s=200, c="red", label="", marker='^')
    # print("São {} pontos de control e {} pontos de tumor".format(pontinho_c, pontinho_t))
    ax.set_xlabel('1st pc', fontsize=18)
    ax.set_ylabel('2st pc', fontsize=18)


    from collections import OrderedDict

    handles, labels = ax.get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), prop={'size': 18})
    plt.rcParams['xtick.labelsize'] = 16
    plt.rcParams['ytick.labelsize'] = 16
    #plt.show()