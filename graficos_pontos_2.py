import matplotlib.pyplot as plt

# GRAFICO DE PONTOS COM MODIFICAÇÕES

#Valores pro Grafico
x = [1, 2, 3, 4, 5] # Colunas dos graficos
y = [2, 3, 7, 4, 1] # Valores das colunas
z = [100, 110, 120, 130, 140] # Variavel com tamanhos = colocar no pontos

titulo = "Grafico de Barras"
eixox = "Eixo X"
eixoy = "Eixo y"

#Legendas Grafico
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#Criar o Grafico
plt.scatter(x,y, label = "Pontos do grafico", color= "Red", marker= "h", s=z)
#Se eu colocar o plot que é o grafico de linhas ele liga os pontos
plt.plot(x,y, color= "black", linestyle= ":")
plt.legend()
#Mostrar o grafico
#plt.show()
#para salvar o grafico
plt.savefig("figura1.png", dpi=300) # fica salvo com esse nome em PNG na pasta do projeto | EM PDF FICA EM VETORIAL E MAIS ALTA QUALIDADE SO ALTRERA "PNG" PARA ".PDF"
