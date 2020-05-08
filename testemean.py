#!/usr/bin/python3
# -*- coding: utf-8 -*-


from dados_xlsx import new_controle, new_tumor
import numpy as np
from scipy import stats
from os import path
from func import save_obj, load_obj

expressaotumor = []
for rowx in new_tumor.keys():
    expressaotumor.append(np.array(new_tumor[rowx]).mean())

expressaocontrole = []
for rowx in new_controle.keys():
    expressaocontrole.append(np.array(new_controle[rowx]).mean())

expressaotumor_log = np.log(np.array(expressaotumor)+1)
expressaotumor_log_mean = expressaotumor_log.mean()
print('média tumor = % s' % expressaotumor_log_mean)
print('geom = % s' % stats.gmean(expressaotumor_log))

expressaocontrole_log = np.log(np.array(expressaocontrole)+1)
expressaocontrole_log_mean = expressaocontrole_log.mean()
print('média controle = % s' % expressaocontrole_log_mean)
print('geom = % s' % stats.gmean(expressaocontrole_log))