#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import pickle
import numpy

def default(o):
    '''
    Algumas vezes salvar em json causa erro por 
    formatação do número.
    Esta função é para certificar que os números
    serão bem formatados
    '''
    if isinstance(o, numpy.int64): return int(o)  
    raise TypeError

def save_obj(obj, name, txt=".json"):
    '''
    Salvar dicionário em formato json
    
    obj: dicionário python
    name: nome do arquivo que será salvo
    txt: formato padrão é json
    '''
    with open(name + txt, 'w') as f:
        json.dump(obj, f, default=default)

def load_obj(name):
    '''
    Load json em formato dicionário
    
    name: nome do arquivo que será aberto
    '''
    with open(name + '.json', 'rb') as f:
        return json.load(f)