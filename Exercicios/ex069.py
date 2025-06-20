# ler o sexo de varias pessoas, a cada pessoa
# cadastrada, o programa deve perguntar
# se o usuario quer continuar
# mostrar:
# quantas pessoaas tem +18
# quantos homenes
# quantas mulheres tem menos de 20#

maior18 = 0
total_homens = 0
mulheres_menos20 = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()

    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos20 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('-' * 30)
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {total_homens} homem(ns) cadastrados.')
print(f'E temos {mulheres_menos20} mulher(es) com menos de 20 anos.')
print('FIM DO PROGRAMA')