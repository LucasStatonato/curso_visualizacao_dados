import matplotlib.pyplot as plt

#BOXPLOT - DIAGRAMA DE CAIXA

import matplotlib.pyplot as plt
import random

vetor = []

for i in range(1000):
    numero_aletorio = random.randint(0,500) #pegar numeros aletorios entre 0 e 50 para adicionar ao vetor
    vetor.append(numero_aletorio)#adicionado ao vetor os numeros aletorios
    
#fazer o diagrama
plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()
plt.savefig("Boxplot.png")