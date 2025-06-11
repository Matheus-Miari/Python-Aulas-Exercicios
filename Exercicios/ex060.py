# ler um numero e mostrar seu fatorial
# #
from time import sleep

num = int(input('Digite um número: '))
fatorial = 1
contador = num
while contador > 0:
    fatorial *= contador
    contador -= 1
    print(f'{fatorial} * {contador} = {fatorial * contador}')
    sleep(0.3)
print(f'O fatorial de {num} é {fatorial}')
