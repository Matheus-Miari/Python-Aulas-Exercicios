# jogar par ou impar com o pc
# interrompe qunado o jogador perder
# mostrando as vitorias consecutivas
# #

import random

vitorias = 0

print('=== JOGO DO PAR OU ÍMPAR ===')

while True:
    jogador = int(input('Digite um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = input('Par ou Ímpar? [P/I] ').strip().upper()

    pc = random.randint(0, 10)
    total = jogador + pc

    print(f'Você jogou {jogador} e o computador {pc}. Total de {total}.')

    if total % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'

    if escolha == resultado:
        print('Você VENCEU!\nVamos jogar novamente...')
        vitorias += 1
    else:
        print('Você PERDEU!')
        break

print(f'GAME OVER! Você venceu {vitorias} vez(es) consecutivas.')
