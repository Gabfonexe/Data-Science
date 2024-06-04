# Listas

cor_cliente = input('Digite a cor desejada: ')
cores = ['verde', 'amarelo', 'azul', 'vermelho', 'roxo']

if cor_cliente.lower() in cores:
  print(f'temos a cor {cor_cliente.lower()} em estoque')
else:
  print(f'Não temos a cor {cor_cliente.lower()} em estoque')