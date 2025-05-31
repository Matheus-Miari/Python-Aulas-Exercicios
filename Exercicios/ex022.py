# CRIE UM PROGRAMA QUE LEIA UM NOME
# E MOSTRE O NOME EM
# MAISCULO
# MINUSCULOS
# QUANTAS LETRAS TEM SEM OS ESPACOS
# QUANTAS LETRAS TEM O PRIMEIRO NOME
#
nome = str(input('Digite seu nome ai boboca: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maisculos {nome.upper()} e minusculos {nome.lower()}')
print(f'Seu nome tem {len(nome)-nome.count(' ')} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')

separa = nome.split()
print(separa)

print(f'Seu primeiro {separa[0]} tem {len(separa[0])} letras')