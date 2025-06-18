#TABUDA DE VARIOS NUMEROS
# UM DE CADA VEZ, PARA CADA VALOR, DIGITADO
# INTERROMPE SE FOR NEGATIVO
from time import sleep

print('--Tabuada--')

n = int(input('Digite um num: '))
cont = 0

while cont <= 10:
    print(f'{n} x {cont} = {n * cont}')
    cont += 1
    sleep(0.2)