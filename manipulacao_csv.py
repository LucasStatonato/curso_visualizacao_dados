import matplotlib.pyplot as plt

#MANIPULÃÇÃO DE DADOS ATRAVES DE UM ARQUIVO CSV

dados = open("populacao_brasileira.csv").readlines()

x= []
y = []

for i in range(len(dados)):
    if i !=0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))
        
plt.title("Crescimento da População Brasileria 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População X 100.000.000")

plt.bar(x,y, color="#e4e4e4")
plt.plot(x, y, color ="k", linestyle="--")
plt.show()
plt.savefig("População Brasileira.png", dpi =300)