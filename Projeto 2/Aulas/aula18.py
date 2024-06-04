# For Loop Nested - loop dentro de loop

# Outer Loop - loop de fora
# Inner Loop - Loop de dentro
valor = 10 

for numero1 in range(1, 6):
  print(f'Produto {numero1}')
  valor = 10
  for numero2 in range(11):
    valor += 5
    print(numero1, valor)