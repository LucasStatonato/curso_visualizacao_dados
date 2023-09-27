import matplotlib.pyplot as plt

#  GRAFICO DE LINHA


#Valores pro Grafico
x = [1,2,5]
y = [2,3,7]

#Titulo
plt.title("Primeiro grafico em Python")

#nomes eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo y")

#Criar o Grafico
plt.plot(x,y)
#Mostrar o grafico
plt.show()