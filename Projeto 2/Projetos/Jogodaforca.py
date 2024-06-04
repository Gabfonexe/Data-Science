import match
# math variavel :
#    case 1 
#palavra

palavra = 'vermelho'
#tentativas
tentativas2 = ""
for vezes in range(len(palavra)):
  tentativas = input('Digite a letra: ')
  if tentativas in palavra:
    for x in tentativas:
      tentativas2 += tentativas
      

      print(f'{(tentativas2)}')
  else:
    print('Você errou')



#gerar _
      
"""for _ in range(len(palavra)):
  print(" ")"""
  
for _ in range(len(palavra)):
  print("-", end='')
