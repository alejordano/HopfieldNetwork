#!/usr/bin/python3
# -*- coding: utf-8 -*-


from dados_xlsx import new_controle, new_tumor, new_controle2
import numpy as np
from os import path
from func import save_obj, load_obj
from scipy.stats.mstats import gmean

expressaotumor = []
for rowx in new_tumor.keys():
    expressaotumor.append(np.array(new_tumor[rowx]).mean())

expressaocontrole = []
for rowx in new_controle.keys():
    expressaocontrole.append(np.array(new_controle[rowx]).mean())

expressaocontrole2 = []
for rowx in new_controle2.keys():
    expressaocontrole2.append(np.array(new_controle2[rowx]).mean())

expressaotumor_log = np.log(np.array(expressaotumor)+1)
expressaotumor_log_mean = expressaotumor_log.mean()
print('média tumor = % s' % expressaotumor_log_mean)
expressaotumor_log_std = expressaotumor_log.std()
print('SD tumor= % s' % expressaotumor_log_std)

expressaocontrole_log = np.log(np.array(expressaocontrole)+1)
expressaocontrole_log_mean = expressaocontrole_log.mean()
print('média controle = % s' % expressaocontrole_log_mean)
expressaocontrole_log_std = expressaocontrole_log.std()
print('SD controle= % s' % expressaocontrole_log_std)

expressaocontrole2_log = np.log(np.array(expressaocontrole2)+1)
expressaocontrole2_log_mean = expressaocontrole2_log.mean()
print('média controle2 = % s' % expressaocontrole2_log_mean)
expressaocontrole2_log_std = expressaocontrole2_log.std()
print('SD controle2= % s' % expressaocontrole2_log_std)

if (path.exists("tratado_binarizado.json")):
    print("Dados de binarização já estão salvos")
    tumor_binarizado = load_obj("tratado_binarizado")
else:
    tumor_binarizado = {}
    controle_binarizado = {}
    controle2_binarizado = {}

    binarizarcontrole = np.vectorize(lambda x: 0 if x < expressaocontrole_log_mean else 1)
    binarizarcontrole2 = np.vectorize(lambda x: 0 if x < expressaocontrole2_log_mean else 1)
    binarizartumor = np.vectorize(lambda x: 0 if x < expressaotumor_log_mean else 1)

    for key in new_tumor.keys():
        tumor_binarizado[key] = list(binarizartumor(np.log(np.array(new_tumor[key])+1)))

    for key in new_controle.keys():
        controle_binarizado[key] = list(binarizarcontrole(np.log(np.array(new_controle[key])+1)))

    for key in new_controle2.keys():
        controle2_binarizado[key] = list(binarizarcontrole2(np.log(np.array(new_controle2[key])+1)))

#print('tumor binarizado = % s' % tumor_binarizado)
#print('controle binarizado = % s' % controle_binarizado)

if __name__ == "__main__":
    print("Preparando gráfico da binarização do controle para plotar")
    # using matplotlib
    import matplotlib.pyplot as plt
    import scipy.stats as mlab
    
    # size of X axis
    x = np.linspace(expressaocontrole_log_mean - 3*expressaocontrole_log_std, expressaocontrole_log_mean + 3*expressaocontrole_log_std)
    # figure will be 10 para 5
    plt.figure(figsize=(20,15))
    # Plotting a normal
    #plt.plot(x,mlab.norm.pdf(x, expressao_log_mean, expressao_log_std)*100,linewidth=7.0)
    # Ploting a rect in the middle
    plt.plot([expressaocontrole_log_mean for x in range(400)], range(400),linewidth=3.0, color = 'red')
    # graph goes from 0 to 550 on Y axis
    plt.ylim([0, 60])
    # informative text -> +1
    plt.text(16, 30, "+1", color='red', fontweight='bold', fontsize=40)
    # informative text -> 0
    plt.text(6, 30, "0", color='red', fontweight='bold', fontsize=40)
    # label X
    plt.xlabel("Log of means of gene's expression", fontsize=20)
    # label Y
    plt.ylabel("Quantity of genes", fontsize=20)
    # increasing fontsize
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=15)
    # plotting a histogram
    plt.hist(x=expressaocontrole_log, bins='auto', color='#0504aa',alpha=0.7, rwidth=0.85)
    #plt.show()

    print("Preparando gráfico da binarização do tumor para plotar")

    # Tamanho do eixo X
    x = np.linspace(expressaotumor_log_mean - 3 * expressaotumor_log_std, expressaotumor_log_mean + 3 * expressaotumor_log_std)
    # Figura será 10 para 5
    plt.figure(figsize=(20, 15))
    # Plotando uma normal
    # plt.plot(x,mlab.norm.pdf(x, expressao_log_mean, expressao_log_std)*100,linewidth=7.0)
    # Plotando uma linha reta no meio
    plt.plot([expressaotumor_log_mean for x in range(400)], range(400), linewidth=3.0, color='red')
    # O gráfico vai do 0 a 550 no eixo Y
    plt.ylim([0, 60])
    # texto informativo -> +1
    plt.text(14.5, 30, "+1", color='red', fontweight='bold', fontsize=40)
    # texto informativo -> 0
    plt.text(6, 30, "0", color='red', fontweight='bold', fontsize=40)
    # label X
    plt.xlabel("Log of means of gene's expression", fontsize=20)
    # label Y
    plt.ylabel("Quantity of genes", fontsize=20)
    # Aumentando o tamanho dos números
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=15)
    # plotando como histograma
    plt.hist(x=expressaotumor_log, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
    plt.show()
