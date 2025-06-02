"""
computador pensar em um numero de 0 a 5
e peca para o usuario tentar descobrir qual
foi o numero pensado
devera escrever na tela se o usuario venceu
ou nao
"""
import random
from time import sleep

print('*'*20)
sleep(0.3)
print('-JOGO DA ADIVINHAÇÃO-')
user_answer = int(input('Advinhe o numero que estou pensando de 0 a 5: '))
number_pc = random.randint(0,5)
if user_answer == number_pc:
    print(f'Vc e fera meu, eu pensei em {number_pc} e voce acertou ! Nice')
else:
    print('Como diria Faustao... ')
    sleep(0.3)
    print(f'EEEERRRRRROOOOU, PENSEI EM {number_pc}')
