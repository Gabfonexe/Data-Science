def obter_nome():
    while True:
        nome = input('Digite seu nome: ')
        if len(nome) > 3:
            return nome
        print('Você deve digitar um nome com mais de 3 letras.')

def obter_idade():
    while True:
        idade = int(input('Digite sua idade: '))
        if 0 <= idade <= 150:
            return idade
        print('Digite um número entre 0 e 150.')

def obter_salario():
    while True:
        salario = int(input('Digite seu salário: '))
        if salario > 0:
            return salario
        print('Digite um número maior que 0.')

def obter_sexo():
    while True:
        sexo = input('Digite seu sexo [f]eminino ou [m]asculino: ')
        if sexo in ['f', 'm']:
            return sexo
        print('Digite a letra [f]eminino ou [m]asculino.')

def obter_estado_civil():
    opcoes = {'s': 'Solteiro', 'c': 'Casado', 'v': 'Viúvo', 'd': 'Divorciado'}
    while True:
        estado_civil = input('Digite seu estado civil: [S]olteiro, [C]asado, [V]iúvo, [D]ivorciado: ').lower()
        if estado_civil in opcoes:
            print(f'Parabéns, você é {opcoes[estado_civil]}')
            return estado_civil
        print(f'Você digitou {estado_civil} e isso não está correto.')

# Obter e exibir informações
nome = obter_nome()
print(f'Seu nome é {nome}')

idade = obter_idade()
print(f'Parabéns, sua idade é {idade}')

salario = obter_salario()
print(f'Parabéns, seu salário é R$ {salario}')

sexo = obter_sexo()
print(f'Parabéns, seu sexo é {sexo}')

estado_civil = obter_estado_civil()
