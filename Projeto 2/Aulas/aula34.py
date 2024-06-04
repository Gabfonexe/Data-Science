#Listas
#armazenar mais de 1 informação em uma variável
#manter a sequencia dos dados em uma variável

numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

numeros.extend(letras) # extendendo a lista, ou seja, add a lista letra na de numeros
print(numeros)


numeross = [1, 2, 3, 4]
print(numeross[2])
itens = [['item 1', 'item 2'], ['item 3', 'item 4']]
print(itens[1][0])