#Unpacking Lists
# Armazenar mais  de uma informação em variáveis
# Manter a sequencia dos dados em uma variável

produtos = ['arroz', 'feijão', 'laranja', 'banana', 5, 6, 7, 8]
#            0           1        2           3

item1, item2, *outros, item8 = produtos
#    essa variável outros faz com que os intens da lista que não estão sendo chamados pela variável especifica, seja englobado na variável outros

print(item1)
print(item2)
print(item8)
print(outros)