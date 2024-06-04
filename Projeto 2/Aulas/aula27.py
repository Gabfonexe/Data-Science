#functions (funções)
#DRY - Don´t Repeat Yourself
#parametro --> arumento
#default - Aquele que vicê define o valor no parametro
#Non-Default - Aquele que você não define o valor no parametro
#Não pode deixar o non-default na frente do default, vai apresentar erro. 

              #non-default    #default
def boas_vindas(nome, quantidade=6):
  print(f'Olá, {nome}')
  print(f'Temos {str(quantidade)} em estoque')

boas_vindas('Marcos')