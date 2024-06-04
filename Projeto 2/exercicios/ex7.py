#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro


n = 20
y = 20
print(n)
for vezes in range(n):
  n -= 1
  if n == 0:
    break
  for vezes2 in range(y):

  

    print(n, end=" ")
  print()
