#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sklearn.preprocessing
from sklearn.decomposition import PCA
from clusters import atratores, atratores_classificacao
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def energy(input_vector):
    '''
    Função de energia
    '''
    input_vector = np.array(input_vector)
    input_vector[input_vector>0.5] = 1
    input_vector[input_vector<=0.5] = 0
    # input_vector = np.random.choice([0, 1], size=(len(teste[0]),len(teste[0])), p=input_vector)
    X = teste
    weight = X.T.dot(X) - 2 * np.eye(len(teste[0]))
    return -0.5 * input_vector.dot(weight).dot(input_vector)

pca = PCA(n_components=2)
pca.fit(atratores)
x = y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(x, y)
energies = map(energy, pca.inverse_transform(zip(np.ravel(X), np.ravel(Y))))

zs = np.array(list(energies))
Z = zs.reshape(X.shape)