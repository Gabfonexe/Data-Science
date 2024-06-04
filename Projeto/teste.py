from turtle import st


nome = input("digite seu nome: ")
idade = input("digite sua idade: ")
linha1 = f"Voce nao e maior de idade, nao podera prosseguir..."
linha2 = f"{nome} voce tem {idade} anos"
#linha3 = f"{nome} voce pesa {a}"
#linha4 = f"seu IMC e : {imc}"
idade_int = int(idade)
if idade_int >= 18:
    a = input("Qual o seu peso? ")
    b = input("Qual a sua altura? ")
    peso = float(a)
    altura = float(b)
    linha3 = f"{nome} voce pesa {peso:.2f} e tem {altura:.2f} metros"
    print(linha3)
    imc = peso / altura ** 2
    linha4 = f"seu IMC e : {imc:.2f}"
    #c = input("Gostaria de calcular seu IMC ? [S] ou [N] : ")
    #if c == "S" or "N":

    
else:
    print(linha1, linha2)
    #linha3 = f"{nome} voce pesa {peso:.2f} e tem {altura:.2f} metros"
c = input("Gostaria de calcular seu IMC ? [S] ou [N] : ")
if c == "S" or "s":
    print(linha4)
else:
    cancelar = "{} voce decidiu cancelar ".format(nome)

...

#interpolar 



start = 0
end = 0
while start < end:
    start += 1
    print(start)