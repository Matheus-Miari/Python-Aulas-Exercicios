# FUNCAO MAIOR()
# RECEBE VARIOS NUMEROS
# ANALISAR E DIZER QUAL FOI O MAIOR
# #
from random import randint

def maior(lista):
    print(f'O maior valor digitado foi {max(lista)}')


valores = []

while True:
    num = int(input('Valor: '))
    valores.append(num)
    resp = str(input('Quer continuar? [S/N]: ')).upper()
    if resp in 'Nn':
        break


print(f'A lista digitada foi {valores}. ')
maior(valores)