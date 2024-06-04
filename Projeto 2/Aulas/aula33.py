#Listas
#armazenar mais de 1 informação em uma variável
#manter a sequencia dos dados em uma variável

cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Belo Horizonte'

#               -4               -3               -2            -1
cidades = ['Rio de Janeiro' ,'São Paulo' , 'Belo Horizonte', 'Goiania']
#                0                1                2             3

cidades[0] = 'Brasilia'

cidades.append('Santa Catarina') # add um item ao final da lista
cidades.remove("Belo Horizonte") # remove um item da lista
cidades.insert(1, 'Nilópolis') # add um item no index indicado, não substitui o antigo.
cidades.pop(3) # remove um item pelo seu index
cidades.sort() # deica em ordem alfabética


print(cidades)