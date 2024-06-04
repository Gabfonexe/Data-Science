#functions (funções)
#DRY - Don´t Repeat Yourself
#Vários Argumentos (xargs)
#Quando coloca * atrás do parametro, siginifica que ele terá vários argumentos (Xargs)

#Criar uma função que some vários números

def soma(*numeros):
  resultado = 0
  for y in numeros:
    resultado += y
  return resultado

w = soma(1,3,4,5,6,7,7)

print(w)

def subtracao(*numeros):
  resultado = 0
  for y in numeros:
    resultado -= y
  return resultado

x = subtracao(1,5,7,9,1,2,4,10)

print(x)

def multiplicacao(*numeros):
  resultado = 1
  for y in numeros:
    resultado *= y
  return resultado

y = multiplicacao(1,2,7,5,8,9)

print(y)

def divisao(*numeros):
  resultado = 1
  for y in numeros:
    resultado /= y
  return resultado

z = divisao(2,4,7,9)

print (z)


