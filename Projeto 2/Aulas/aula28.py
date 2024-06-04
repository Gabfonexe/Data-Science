#functions (funções)
#DRY - Don´t Repeat Yourself

#Print - realiza uma tarefa
#Return - calcula e retorna um valor. Armazena os dados

def client1(nome):
  print(f'olá {nome}')


client1('Maria')


def client2(nome):
  return(f'Olá {nome}')


print(client2('josé')) # precisa do print para chamar o valor da function, pois tem o return nessa
