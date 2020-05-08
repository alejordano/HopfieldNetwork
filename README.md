# HopfieldNetwork
Codes used for Hopfield Network analysis
1 - func.py. Função criada para salvar objetos
2 - dados_xlsx.py - Leitura de arquivos em excel. grupo controle e grupo tratado.
3 - pacientes_formula.py - classificação de pacientes de acordo com seu grupo e mudança na organização dos dados. 
4 - binaring.py - Binarização do log dos valores de expressão gênica c base na média de cada grupo. 
5 - clusters.py - Definição de atratores. Análise PCA e t-SNE. 
6 - Hopfield_teste.py - testa quantas amostras foram para os atratores corretos, errados e não convergiram para nenhum dos atratores.
7 - energy.py - criação do campo de energia de Hopfield.
8 - density.py - determinação dos parâmetros de interatoma e densidade para priorização de alvos. 
9  - go.py - determinação do parâmetro gene ontology para priorização de alvos. 
10 - parametro_conservador.py - determina em quantos pacientes um alvo é ativo na amostra tumoral e inativo na amostra controle. 
11 - Intervenção_energia.py - testa as alterações necessárias para retirar as amostras de dentro da bacia de atração. 
12 - simulação_trastuzumabe.py - identifica os genes com estados diferentes entre as amostras bulk tratado e controle 1; muda os estados do controle 1 de acordo com o estado do gene na amostra tratada. 
