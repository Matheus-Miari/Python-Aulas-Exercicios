# calcular a soma entre todos os numeros
# impares que sao multiplos de 3
# e que se encontram no intervalo de 1 ate 500#

soma = 0
cont = 0
for c in range(1,501):
    if c % 2 == 1 and c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print(f'Somatorio: {soma}')
print(f'Todos os valores: {cont}')