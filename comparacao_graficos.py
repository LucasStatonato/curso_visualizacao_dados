import matplotlib.pyplot as plt

#COMPARAÇÃO DE VALORES EM UM GRAFICO DE BARRA

#Valores pro Grafico
x1 = [1, 2, 3, 4, 5] # Colunas dos graficos
y1 = [2, 3, 7, 1, 0] # Valores das colunas

x2 = [2, 4, 6, 8, 10] # Colunas dos graficos
y2 = [5, 1, 3, 7, 4] # Valores das colunas

titulo = "Grafico de Barras"
eixox = "Eixo X"
eixoy = "Eixo y"

#Legendas Grafico
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#Criar o Grafico
plt.bar(x1,y1, label = "Grupo 1")
plt.bar(x2,y2, label = "Grupo 2")
#mostrar legenda
plt.legend()
#Mostrar o grafico
plt.show()