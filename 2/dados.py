import csv

def carregar_arquivo():
    X = []
    Y = []
    arquivo = open('arquivo.csv','r')
    leitor = csv.reader(arquivo)
    next(leitor)
    for home,como_funciona,contato,comprou in leitor:
        X.append([int(home),int(como_funciona),int(contato)])
        Y.append(int(comprou))
    return X, Y