# exercicio funcao e parametros
from sys import base_prefix


def borda(s1):
    tan = len(s1)
    if tan:
        print('_','=' * tan, '_')
        print('|',s1,'|')
        print('_', '=' * tan, '_')

#chama
borda('Aceitas pix')
borda('Colocando uma quantidade grande de caracteres')

# multipla por tan = quantidade de caracteres