import matplotlib.pyplot as plt

#ANALISE DE DADOS GENETICOS

entrada = open("C:/Users/PC Lucas/Documents/textoimage py/teste email/bacteria.fasta").read()
saida  = open("bacteria.hmtl","w")

#criar um dicionario de contagem

cont = {}

# CRIAR UM LAÇO FORK QUE PERCORRE TODOS OS VALORES E JUNTAM EM DUPLAS COM O VALOR 0 SEM SOMATORIA 


for i in ['A', 'T', 'C', 'G']: #primeira lista
    for j in ['A', 'T', 'C', 'G']: #segunda lista
        cont[i+j] = 0  #justa as duas lista com o valor 0


entrada = entrada.replace("\n", "") #REMOVE AS QUEBRAS DE LINHAS

#Começar a preencher as duplas E calcular quantas duplas tem
for k in range(len(entrada)-1):          #cria uma lista que vai percorrer toda a entrada - len ve o tamanho (-1 por o ultimo valor não tem par)
    cont[entrada[k]+entrada[k+1]] +=1    #vai procurar a posiçao que encontra e vai adicionar 1 na contagem
    
print(cont)

#vamos passar para o HTML para visualizar melhor a quantidade de duplas

#inicio HTML

#Cria um novo contador

i = 1

#criar um laço de repetição para varrer os resultados
for k in cont: #varrendo o dcionario cont e cada chave sera armazenado em K
    transparencia = cont[k]/max(cont.values())#pega os valores da lista e divide pelo o maior para assim ter uma % e dividir e ter uma transparecencia
    saida.write("<div style='width:100px; border:1px solid #111; color: #fff; height:100px; float: left; background-color:rgba(0,0,0, "+str(transparencia)+"')>"+k+"</div>")#vou printar meu resultado e manipular com hmtl
    
    if i%4 == 0: #divide para uma quebra de linha ate 4 quadrados
        saida.write("<div style='clear:both'></div>")
        
    i+=1 #precisa icrementar 1 para funcionar
    
saida.close()
