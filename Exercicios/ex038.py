#programa que leia que leia dois numeros inteiros
# e compare-os
# mostrando o maior, menor e se sao iguais#

n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))

if n1 > n2:
    print(f'{n1} > {n2}')
elif n2 > n1:
    print(f'{n2} > {n1}')
else:
    print('Numeros iguais')