# ajuda na mega sena  a criar
# palpites
# perguntar quantos jogos serao jogados
# e vai sortear 6 numeros
# de 1  60 para cada jogo
# cadastrando em uma lista composta\
# numeros nao podem repetir#
from random import randint
from time import sleep
jogoCompleto = []  # iniciei  a lista do jogo completo
print('='*50)
titulo = 'Bem Vindo ao gerador de jogos'
print('{:-^50}'.format(titulo))
print('='*50)
qtdJogos = int(input('Quantos jogos vc vai jogar: '))  # qtd de jogos
for i in range(qtdJogos): # para cada item no range de quantidade de jogo
    jogo = [] # inicia uma lista de jogo
    while len(jogo) < 6: # enquanto quantidade de jogo menor que 6 -- 6 numeros da mega
        numero = randint(1,60) # randomizar os 6 numeros
        if numero not in jogo: # se o numero nao tiver no jogo, acrescente
            jogo.append(numero) # add
    jogoCompleto.append(jogo) # add o jogo no jogoCompleto
for i, jogo in enumerate(jogoCompleto, 1): # para cada item, jogo no jogo completo
    print(f'Jogo {i}: {sorted(jogo)}') # printa o numero/indice do jogo  e o jogo
    sleep(.5)
