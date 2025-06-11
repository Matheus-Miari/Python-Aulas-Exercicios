# ler varios numeros inteiros
# mostre a media entre todos eles, qual foi o maior
# e o menor, o programa deve perguntar se ele quer continuar
# ou nao a digitar valores #
soma = 0
cont = 0
continuar = 'S'
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = input('Quer continuar? [S/N] ').strip().upper()
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior número foi {maior} e o menor foi {menor}')
print('~' * 30)
