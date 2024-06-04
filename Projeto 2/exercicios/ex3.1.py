def qtd_nome():
    nome = input('Digite seu nome: ')
    if len(nome) <= 3:
      print(f'Você deve digitar um nome com mais de 3 letras.')
      novo_nome = input('Digite seu nome: ')
      while len(novo_nome) <= 3:
        print(f'Você deve digitar um nome com mais de 3 letras.')
        novo_nome = input('Digite seu nome: ')
        if len(novo_nome) > 3:
          print(f'Seu nome é {novo_nome}')
    else:
        print(f'Seu nome é {nome}')


qtd_nome()


def idade():
  idade = int(input('Digite sua idade: '))
  if idade < 0 or idade > 150:
    print('Digite um número entre 0 e 150')
  novo_idade = int(input('Digite sua idade: '))
  while novo_idade < 0 or novo_idade > 150:
    print('Digite um número entre 0 e 150')
    novo_idade = int(input('Digite sua idade: '))
    if novo_idade >= 0 or novo_idade <= 150:
      print(f'Parabéns, sua idade é {novo_idade}')
  else:
    print(f'Parabéns, sua idade é {idade}')


idade()


def salario():
  salario = int(input('Digite seu salário: '))
  if salario <= 0:
   print('Digite um número maior que 0')
   novo_salario = int(input('Digite seu salário: '))
   while novo_salario <= 0:
    print('Digite um número maior que 0')
    novo_salario = int(input('Digite seu salário: '))
    if novo_salario > 0:
      print(f'Parabéns, seu salário é R$ {novo_salario}')
  else:
    print(f'Parabéns, seu salário é R$ {salario}')


def sexo():
  sexo = input('Digite seu sexo [f]eminino ou [m]asculino :')
  if sexo != 'f' and sexo != 'm':
    print('Digite a letra [f]eminino ou [m]asculino')
    novo_sexo = input('Digite novamente [f] ou [m] : ')
    while novo_sexo != 'f' and novo_sexo != 'm':
      print('Digite a letra [f]eminino ou [m]asculino')
      novo_sexo = input('Digite novamente [f] ou [m] : ')
      if novo_sexo == 'f' or novo_sexo == 'm':
        print(f'Parabéns, seu sexo é {novo_sexo}')
  else:
    print(f'Parabéns, seu sexo é {sexo}')


sexo()


def estado_civil():
  estado_civil = input('Digite seu estado civil: [S]olteiro, [C]asado, [V]iúvo, [D]ivorciado: ')
  if estado_civil == 's':
   print(f'Parabéns, você é {estado_civil}olteiro')
  elif estado_civil == 'c':
   print(f'Parabéns, você é {estado_civil}asado')
  elif estado_civil == 'v':
   print(f'poxa, infelizmente você é {estado_civil}iúvo')
  elif estado_civil == 'd':
   print(f'Vejo aqui que você é {estado_civil}ivorciado')
  else:
      print(f'você digitou {estado_civil} e isso não está correto')
      novo_estado_civil = input('Digite novamente [s], [c], [v] ou [d] : ')
      if novo_estado_civil == 's' or estado_civil == 'c' or estado_civil =='v' or  estado_civil == 'd':
         print(f'Seu estado civil é {novo_estado_civil}')
      else:
          novo_estado_civil = input('Digite seu estado civil: [S]olteiro, [C]asado, [V]iúvo, [D]ivorciado: ')
          print(novo_estado_civil)
          while novo_estado_civil != 's' or novo_estado_civil != 'c' or novo_estado_civil != 'v' or novo_estado_civil != 'd':
              print(f'você digitou {novo_estado_civil} e isso não está correto')
              a1 = input('Digite novamente [s], [c], [v] ou [d] : ')
              if a1 == 's' or a1 == 'c' or a1 == 'v' or a1 == 'd':
                  print(f'Vejo aqui que você é {novo_estado_civil}')
                  break
              

estado_civil()