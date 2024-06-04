def get_input(prompt, condition, error_message):
    value = input(prompt)
    while not condition(value):
        print(error_message)
        value = input(prompt)
    return value

nome = get_input('Digite seu nome: ', lambda x: len(x) > 3, 'Você deve digitar um nome com mais de 3 letras.')
idade = int(get_input('Digite sua idade: ', lambda x: 0 <= int(x) <= 150, 'Digite um número entre 0 e 150'))
salario = int(get_input('Digite seu salário: ', lambda x: int(x) > 0, 'Digite um número maior que 0'))
sexo = get_input('Digite seu sexo [f]eminino ou [m]asculino :', lambda x: x in ['f', 'm'], 'Digite a letra [f]eminino ou [m]asculino')
estado_civil = get_input('Digite seu estado civil: [S]olteiro, [C]asado, [V]iúvo, [D]ivorciado: ', lambda x: x in ['s', 'c', 'v', 'd'], 'Digite novamente [s], [c], [v] ou [d] : ')

print(f'Seu nome é {nome}')
print(f'Parabéns, sua idade é {idade}')
print(f'Parabéns, seu salário é R$ {salario}')
print(f'Parabéns, seu sexo é {sexo}')
print(f'Seu estado civil é {estado_civil}')
