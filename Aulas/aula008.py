# MODULOS
# para incluir algo se utiliza o import
# exemplos = import comida
# from comida import picanha // economiza memoria

# import math   # importa tudo de math
from math import sqrt  # importa a funcao  de sqrt

num = int(input('Digite um num: '))
raiz = sqrt(num)
print(f'A raiz de {num}: {raiz:.2f}')