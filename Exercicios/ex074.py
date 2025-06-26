# GERAR 5 NUMEROS ALEATORIOS
# E GUARDAR NA TUPLA
# MOSTRAR A LISTA
# INDICAR O MAIOR E O MENOR

from random import randint

tupla_aleatoria = (randint(1,10),randint(1,10),
                   randint(1,10),randint(1,10),
                   randint(1,10),)
print(f'Numeros sorteados: ')

for n in tupla_aleatoria:
    print(n, end=' ')
print()
print(f'Maior: {max(tupla_aleatoria)}')
print(f'Menor: {min(tupla_aleatoria)}')