#!/usr/bin/python3# -*- coding: utf-8 -*-

import xlrd
import numpy as np
from os import path
from func import save_obj, load_obj

# Vamos checar se já temos os dados salvos Já que ver toda a tabela o tempo inteiro demora
if (path.exists("new_datacontroleAle.json") and path.exists("new_datatreatedAle.json") and
            path.exists("new_datacontrole2Ale.json")):
    print("Dados de controles e tumor já estão salvos")
    # Dicionário com as expressões gênicas
    # de cada paciente no controle
    new_controle = load_obj("new_datacontroleAle")
    new_controle2 = load_obj("new_datacontrole2Ale")
    # Dicionário com as expressões genéticas
    # de cada paciente no tumor
    new_tumor = load_obj("new_datatreatedAle")
else:
    print("Abrindo a planilha de dados xlsx")
    filename = "DEGSCBULK.xlsx"
    dados = xlrd.open_workbook(filename)
    # Vamos salvar os genes nestes dict
    genes_Ensembl = []
    # genes_name = {}

    # Dicionário com as expressões gênicas
    # de cada paciente no controle
    new_controle = {}
    # Ir para a primeira aba dessa planilha
    # a primeira aba é onde tem os dados de controle
    sheet_controle = dados.sheet_by_index(0)
    # A partir da segunda linha dessa aba, começar a iterar
    for rowx in range(1, sheet_controle.nrows):
        # Todos os valores daquela linha:
        row = sheet_controle.row_values(rowx)
        # primeira coluna é o nome do gene em Uniprotkb
        # genes_uniprotkb.append(row[0])
        # segunda coluna é o nome do gene normalmente usado
        # vamos criar um dicionário fazendo referência entre os dois
        # genes_name[row[1]] = row[0]
        # primeira coluna é o nome do gene em Uniprotkb
        genes_Ensembl.append(row[0])

        # vamos iterar em todas as colunas da linha
        new_list = []
        for x in range(1, len(row)):
            # a cada 1 colunas temos um dado novo
            # lembrando que python começa no zero
            # if (x + 1)%1 == 0:
            new_list.append(row[x])
        # para aquele gene row[0] temos as seguintes expressões
        new_controle[row[0]] = new_list
    # Salvando os dados de controle
    save_obj(new_controle, "new_datacontroleAle")

    new_controle2 = {}
    # Ir para a primeira aba dessa planilha
    # a primeira aba é onde tem os dados de controle
    sheet_controle2 = dados.sheet_by_index(2)
    # A partir da segunda linha dessa aba, começar a iterar
    for rowx in range(1, sheet_controle2.nrows):
    # Todos os valores daquela linha:
        row = sheet_controle2.row_values(rowx)
    # primeira coluna é o nome do gene em Uniprotkb
    # genes_uniprotkb.append(row[0])
    # segunda coluna é o nome do gene normalmente usado
    # vamos criar um dicionário fazendo referência entre os dois
    # genes_name[row[1]] = row[0]
    # primeira coluna é o nome do gene em Uniprotkb
        genes_Ensembl.append(row[0])

        # vamos iterar em todas as colunas da linha
        new_list = []
        for x in range(1, len(row)):
        # a cada 1 colunas temos um dado novo
        # lembrando que python começa no zero
        # if (x + 1)%1 == 0:
            new_list.append(row[x])
            # para aquele gene row[0] temos as seguintes expressões
        new_controle2[row[0]] = new_list
            # Salvando os dados de controle
    save_obj(new_controle2, "new_datacontrole2Ale")

    # Dicionário com as expressões gênicas
    # de cada paciente no tumor
    new_tumor = {}
    # Ir para a segunda aba dessa planilha
    # a segunda aba é onde tem os dados de tumor
    sheet_tumor = dados.sheet_by_index(1)
    # A partir da segunda linha dessa aba, começar a iterar
    for rowx in range(1, sheet_tumor.nrows):
        # Todos os valores daquela linha
        row = sheet_tumor.row_values(rowx)
        new_list = []
        # vamos iterar em todas as colunas da linha
        for x in range(1, len(row)):
            # a cada 1 colunas temos um dado novo
            # lembrando que python começa no zero
            # if (x + 1)%1 == 0:
            new_list.append(row[x])
        # para aquele gene row[0] temos as seguintes expressões
        new_tumor[row[0]] = new_list
    # Salvando os dados de tumor
    save_obj(new_tumor, "new_datatreatedAle")

print("Carregados dados de Tratado e Controles")