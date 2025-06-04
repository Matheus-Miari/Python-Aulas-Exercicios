# while == enquanto for verdadeiro
# faca

from time import sleep

count = 0  # contador
""" while count <= 5:  # enquanto contador menor igual a 5, print o contador
    print(count)  # print
    count =  count + 1  # incrementa 1 no contador = acumuladora
    sleep(1) """

inicial = int(input('Digite o numero inicial: '))
final = int(input('Digite o numero final: '))

x = inicial
while (x <= final):
    if (x % 2 == 0): # verifica se o numero == par
        print(x)
    x = x + 1