#!/usr/bin/python
# -*- coding: utf-8 -*-

from binarying import tumor_binarizado, controle_binarizado, controle2_binarizado
import numpy as np

def pacientes_binarizados():
    '''
    Vamos retornar uma lista com todos os pacientes
    e suas respectivas expressões genéticas
    binarizadas
    '''
    tratado_binarizado = tumor_binarizado
    pacientes = []
    classificacao = []
    # genes que vamos utilizar
    # vamos descobrir o número de pacientes
    # a partir do tamanho da lista de expressoes de um gene
    n_pacientes = len(tratado_binarizado[list(tratado_binarizado.keys())[0]])
    # para cada paciente
    for x in range(n_pacientes):
        # A lista controle e tumor do paciente
        paciente_tratado = []
        # para cada gene do fold chain
        for gene in tratado_binarizado.keys():
            # adicionar aquele gene ao dado do paciente
            # o gene do paciente sempre está na
            # posição X, a posição não muda
            paciente_tratado.append(tratado_binarizado[gene][x])
        # depois de adicionar todos os genes
        # de um paciente. Adicionamos a lista
        # do paciente em uma lista de todos
        pacientes.append(paciente_tratado)
        classificacao.append(1)

    n_pacientes = len(controle_binarizado[list(controle_binarizado.keys())[0]])
    # para cada paciente
    for x in range(n_pacientes):
        # A lista controle e tumor do paciente
        paciente_controle = []
        # para cada gene do fold chain
        for gene in controle_binarizado.keys():
            # adicionar aquele gene ao dado do paciente
            # o gene do paciente sempre está na
            # posição X, a posição não muda
            paciente_controle.append(controle_binarizado[gene][x])
        # depois de adicionar todos os genes
        # de um paciente. Adicionamos a lista
        # do paciente em uma lista de todos
        pacientes.append(paciente_controle)
        classificacao.append(0)


    n_pacientes = len(controle2_binarizado[list(controle2_binarizado.keys())[0]])
    # para cada paciente
    for x in range(n_pacientes):
        # A lista controle e tumor do paciente
        paciente_controle2 = []
        # para cada gene do fold chain
        for gene in controle2_binarizado.keys():
            # adicionar aquele gene ao dado do paciente
            # o gene do paciente sempre está na
            # posição X, a posição não muda
            paciente_controle2.append(controle2_binarizado[gene][x])
        # depois de adicionar todos os genes
        # de um paciente. Adicionamos a lista
        # do paciente em uma lista de todos
        pacientes.append(paciente_controle2)
        classificacao.append(2)

    n_pacientes = len(samples)
    # para cada paciente
    for x in range(n_pacientes):
        pacientes.append(sample[x])
        classificacao.append(3)


    return pacientes, classificacao