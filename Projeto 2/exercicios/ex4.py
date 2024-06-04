
#num1 = int(input('Digite um número para calcular o fatorial: '))

#x = 0
"""while num1 > 0 :
  x += num1
  resultado = 1 * x
  x += (x-1)
  if x == 1:"""
    
 
#for y in range(num1):
  #for z in range()

"""x += num1
  resultado = 1 * x
  x = 0
  x += (x-1)
  print(resultado)
"""



"""def f(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  if n > 1:
    return f(n-1)*n
  


  
print(f(6))"""


x = int(input('Digite um valor inteiro: '))
y = x
soma = 0
for vezes in range(x):
  resultado = x * y
  y -= 1
  soma += resultado
  print(f'{x} x {y + 1} = ', resultado)

print(f'A soma dos produtos é {soma}')


"""import math

num = int(input('Digite o número: '))
print(math.factorial(num))

"""