import matplotlib.pyplot as plt

#GRAFICO DE PONTOS

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
plt.scatter(x,y, label ="Meus pontos do grafico", color ="black")
#Se eu colocar o plot que é o grafico de linhas ele liga os pontos
plt.plot(x,y, color= "r")
plt.legend()
#Mostrar o grafico
plt.show()