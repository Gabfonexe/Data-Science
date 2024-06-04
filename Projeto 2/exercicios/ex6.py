#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.





populacao_a = int(input('Digite a quantidade de pessoas da cidade A:  '))
taxa_crescimento_a = int(input('Digite a taxa de crescimento em ''%'' da A:  '))
populacao_b = int(input('Digite a quantidade de pessoas da cidade B:  '))
taxa_crescimento_b = int(input('Digite a taxa de crescimento ''%'' da B:  '))


  
anos = 0
porcent_a = (taxa_crescimento_a/100)
porcent_b = (taxa_crescimento_b/100)

while populacao_a < populacao_b:
  nova_populacao_a = populacao_a * porcent_a
  nova_populacao_b = populacao_b * porcent_b
  populacao_a += nova_populacao_a
  populacao_b += nova_populacao_b
  anos += 1
    
  
print(f'{anos} anos')
print(f'População da cidade A: {int(populacao_a)} Pessoas')
print(f'População da cidade B: {int(populacao_b)} Pessoas') 













#a = 80000
#b = 200000
#taxa_a = (3/100)
#taxa_b = (1.5/100)
#anos = 0
#
#while a < b:
#  nova_populacao_a = a * taxa_a 
#  nova_populacao_b = b * taxa_b 
#  a += nova_populacao_a
#  b += nova_populacao_b
#  anos += 1
#  
#
#print(f'{anos} anos')
#print(f'População da cidade A: {int(a)} Pessoas')
#print(f'População da cidade B: {int(b)} Pessoas')