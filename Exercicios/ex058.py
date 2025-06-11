# pc pensar em um numero que 0 e 10
# so que o jogador vai tentar adivinhar ate
# acettas, mostrando no final quantos
# palpites foram necessario para vencer#

from random import randint

pc_num = randint(0,10)
user = 99
cont = 0
while user != pc_num:
    user = int(input('Advinhe o numero: '))
    cont += 1
print(f'Ate que enfim... \n Pensei: {pc_num} e Voce: {user} \n Precisou de {cont} numeros')
