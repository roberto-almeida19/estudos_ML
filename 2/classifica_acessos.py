from dados import carregar_arquivo
X,Y = carregar_arquivo()

treino_dados = X[:90]
treino_marcacao = Y[:90]

teste_dados = X[:-9]
testa_marcacao = Y[:-9]

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacao)
resultado = modelo.predict(teste_dados)

diferenca = resultado - testa_marcacao

acertos = [d for d in diferenca if d == 0]
total_acertos = len(acertos)
elementos = len(X)
taxa_de_acerto = total_acertos * 100 / elementos
print(taxa_de_acerto)