# While Loop

# Publicar um produto com comissão de 10% se for acima de R$20



'''while True:
  
  valor = input('Digite o valor do seu Produto: ')

  if valor == str:
    print(f'Você digitou {valor}, isso não é um número')

  elif valor == int:
    if valor > 20:
        while valor > 20:
          valor = (valor * 0.10) + valor
          print(f'O valor final do produto é R$ {valor}')
          break
    elif valor <= 20:
        print('Não há mudança no valor do produto ')

    else:
        print('Você Não Digitou um número, Digite novamente o valor')'''


valor = int(input("Digite o valor do produto em R$ "))

while valor > 20:
  valor = (valor * 0.10) + valor
  print(f'O valor final do seu produto será de R$ {valor}')
  break


