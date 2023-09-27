import matplotlib.pyplot as plt

#DE GRAFICO DE BARRA

#Valores pro Grafico
x = [1, 2, 3, 4, 5] # Colunas dos graficos
y = [2, 3, 7, 4, 1] # Valores das colunas

titulo = "Grafico de Barras"
eixox = "Eixo X"
eixoy = "Eixo y"

#Legendas Grafico
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#Criar o Grafico
plt.bar(x,y)
#Mostrar o grafico
plt.show()

