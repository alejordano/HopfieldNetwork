#!/usr/bin/python3# -*- coding: utf-8 -*-

import xlrd
import numpy as np
from os import path
from func import save_obj, load_obj

# Is all data saved? 
if (path.exists("new_datacontroleAle.json") and path.exists("new_datatreatedAle.json") and
            path.exists("new_datacontrole2Ale.json")):
    print("Dados de controles e tumor já estão salvos")
    # Dicionary with all genic expression from each control patient
    new_controle = load_obj("new_datacontroleAle")
    new_controle2 = load_obj("new_datacontrole2Ale")
    #  Dicionary with all genic expression from each tumor patient
    new_tumor = load_obj("new_datatreatedAle")
else:
    print("Abrindo a planilha de dados xlsx")
    filename = "DEGSCBULK.xlsx"
    dados = xlrd.open_workbook(filename)
    # save genes in dict
    genes_Ensembl = []
    # genes_name = {}

    #  Dicionary with all genic expression from each control patient
    new_controle = {}
    # Go to first tab of this sheet where we have control data. 
    sheet_controle = dados.sheet_by_index(0)
    # Start analysis from second row of this tab 
    for rowx in range(1, sheet_controle.nrows):
        # all values from that row:
        row = sheet_controle.row_values(rowx)
        # First column is the name of the gene in Uniprot 
        # genes_uniprotkb.append(row[0])
        # Second column is the name of the gene symbol 
        # creating dictionary reference between the two.
        # genes_name[row[1]] = row[0]
        genes_Ensembl.append(row[0])

        # Analyse all columns from row
        new_list = []
        for x in range(1, len(row)):
            # from each column we have a new state
            # if (x + 1)%1 == 0:
            new_list.append(row[x])
        # for gene row[0] we have
        new_controle[row[0]] = new_list
    # saving control data
    save_obj(new_controle, "new_datacontroleAle")

#all again from control2
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

# all again for tumor
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
