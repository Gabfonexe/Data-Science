'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

login = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if login == senha:
  print(f'Nome de usuário e senhas iguais não são permitidos')
  while login == senha:
    print('Digite novamente as novas credencias, sem repetir')
    novo_login = input("Digite seu nome de usuário: ")
    novo_senha = input("Digite sua senha: ")
    if novo_login != novo_senha:
      print(f'Parabéns, seu login [ {novo_login} ] e sua nova senha [ {novo_senha} ] foram cadastrados!')
      break
    else:
      print("DIgite novamente...")
else:
  print(f'Parabéns, seu login [ {login} ] e sua nova senha [ {senha} ] foram cadastrados!')
