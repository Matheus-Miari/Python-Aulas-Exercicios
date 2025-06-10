# ler nome, idade e sexo de 4 pessoas
# no final mostre:
#  media de idade do grupo
#  homem mais velho
#  quantas mulheres tem menos de 20 #

soma_idade = 0
media_idade = 0
nome_homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_vinte = 0

for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    soma_idade += idade

    if sexo == 'M':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome
    elif sexo == 'F':
        if idade < 20:
            mulheres_menos_vinte += 1

media_idade = soma_idade / 4

print(f'\nA média de idade do grupo é {media_idade:.1f} anos.')
if nome_homem_mais_velho:
    print(f'O homem mais velho é {nome_homem_mais_velho} com {idade_homem_mais_velho} anos.')
else:
    print('Não há homens no grupo.')
print(f'Ao todo são {mulheres_menos_vinte} mulher(es) com menos de 20 anos.')
