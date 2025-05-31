#PROGRAMA LEIA UM NUMERO DE 0 A 9999
# E MOSTRE NA TELA CADA UM DOS DIGITOS
# SEPARADOS
# EM UNIDADE, DEZENA CENTENA E MILHAR#

n1 = int(input('Digite um numero de 0 a 9999: '))

u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print(f'Analisando o numero: {n1}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')