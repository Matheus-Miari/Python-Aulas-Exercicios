# jogar par ou impar com o pc
# interrompe qunado o jogador perder
# mostrando as vitorias consecutivas
# #

import random

contador_de_vitoria = 0

while True:
    jogador = int(input('Digite um numero: '))
    escolha = input('Par ou Impar: ').strip().upper()

    while escolha not in ['P', 'I']:
        escolha = input('Escolha inválida. Par ou Ímpar? [P/I]: ').strip().upper()

    pc_num = random.randint(0,10)
    soma = jogador + pc_num

    print(f'Você jogou {jogador} e o computador jogou {pc_num}. Total: {soma}.')

    if (soma % 2 == 0 and escolha == 'P') or (soma % 2 != 0 and escolha == 'I'):
        print('Vc venceu, vamos dnv: \n')
        contador_de_vitoria += 1
    else:
        print('Vc perdeu mané..')
        break
print(f'Jogo encerrado. Vc venceu {contador_de_vitoria} vezes consecutivas')