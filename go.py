list_go = []
with open("listaGO.txt", "r") as file:
    for line in file:
        list_go.append(line.strip())
        
dict_gene = {}
with open("classificacaopanther.txt", "r") as file:
    for line in file:
        if len(line.split("\t")) > 1:
            gene = line.split("\t")[1]
            dict_gene[gene] = []
            informacao = "\t".join(line.split("\t")[1:])
            for go in list_go:
                if go.lower() in informacao.lower():
                    dict_gene[gene] = dict_gene[gene] + [go]
            list_go.append(line.strip())

resultados = dict_gene.items()

import xlrd

print("Abrindo a planilha de dados xlsx")
filename = "FPKMmamaAle.xlsx"
dados = xlrd.open_workbook(filename)
coluna_gene = []
sheet_controle = dados.sheet_by_index(0)
for rowx in range(1, sheet_controle.nrows):
    # Todos os valores daquela linha:
    row = sheet_controle.row_values(rowx)
    coluna_gene.append(row[0].split(".")[0])

def procurar_posicao(gene):
    for x in range(len(coluna_gene)):
        if "," in coluna_gene[x]:
            print(coluna_gene[x])
            for ensemble in coluna_gene[x].split(","):
                if ensemble.strip() == gene:
                    return x
        if coluna_gene[x] == gene:
            return x
    print(gene)

parametro_go = []
for resultado in dict_gene.items():
    parametro_go.append([len(resultado[-1]), procurar_posicao(resultado[0].split("=")[-1])])
    print("{}: {}".format(resultado[0].split("=")[-1], len(resultado[-1])))


print(parametro_go)



