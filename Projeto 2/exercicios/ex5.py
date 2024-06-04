#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

a = 80000
b = 200000
taxa_a = (3/100)
taxa_b = (1.5/100)
anos = 0

while a < b:
  nova_populacao_a = a * taxa_a 
  nova_populacao_b = b * taxa_b 
  a += nova_populacao_a
  b += nova_populacao_b
  anos += 1
  

print(f'{anos} anos')
print(f'População da cidade A: {int(a)} Pessoas')
print(f'População da cidade B: {int(b)} Pessoas')




"""populacao_a = a * taxa_a + nova_populacao_a
  populacao_b = b * taxa_b + nova_populacao_b
 a += populacao_a
  b += populacao_b"""






