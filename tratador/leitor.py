import csv

def carregar_arquivo():

    X = []
    Y = []
    arquivo = open('cursos.csv','r')
    leitor = csv.reader(arquivo)
    next(leitor)
    for home,busca,logado,comprou in leitor:
        X.append([int(home),(busca),int(logado)])
        Y.append(int(comprou))
    return X, Y
pass