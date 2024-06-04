#functions (funções)
#DRY - Don´t Repeat Yourself
#Vários Argumentos (xargs) identificando os parametros
#Quando colocamos ** no porametro, podemos dizer que será possivel adicionar vários argumentos para cada argumento, sem a necessidade de haver mudança no parametro.

#Criar uma função que armazena números e strings (dados)

def agencia(**carro):
  return carro

w = agencia (cor = 'preto', modelo = 1.0, altura = 2, largura = 4 )
x = agencia (cor = 'branco', modelo = 1.3, altura = 2, largura = 4 )
y = agencia (cor = 'branco', altura = 2, largura = 4 )
z = agencia ( modelo = 1.3, altura = 2, largura = 4 )

print(w)
print(x)
print(y)
print(z)
