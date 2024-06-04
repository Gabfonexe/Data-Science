# Usando zip em Listas

cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]



duas_listas = zip(cores, valores)

print(list(duas_listas)) #aqui tem que usar o list para converter novamente em lista



var =  list('amor') # a funcao list itera sobre uma string e transforme uma string em varias 
print(var)