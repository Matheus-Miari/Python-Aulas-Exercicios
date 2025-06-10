# mostrar na tela uma contagem
# regressiva pra o estouro de fogos
# 10 ate 1 com 1 segundo de intervalo#

'''CONTAGEM REGRESSIVA'''
from time import sleep

for c in range (10, -1, -1):
    print(c)
    sleep(1)
print('Feliz ano novo chara !!!')