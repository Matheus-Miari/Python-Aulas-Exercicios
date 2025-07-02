# sete valores numericos
# cadastrar em uma unica lista e manter
# separdos os valores pares e impares
# no final mostrar os valores pares e impares em
# ordem crescente#

valores = []
pares = []
impares = []

for num in range(0,7):
    valores.append(int(input('Digite o valor: ')))

for num in valores:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Lista: {valores}')
print(f'Pares: {sorted(pares)}')
print(f'Impares: {sorted(impares)}')
