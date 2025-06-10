# LACOS  - - - AULA TEORICA
# laco nome no intervalo(1,10)
#   passo
# pega  #
from time import sleep

# for c in range(1,10):
#    passo
# pega

# for c in range(5,0, -1):  ## para c no  intervalo de (5 a 0, pule - 1 a cada repiticao)
   # print(c)   # contagem regressiva de 5 a 0
    #sleep(1)
# print('Cabou')

''' i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
    sleep(0.5)
print('Fim')'''

s = 0
for c in range(0,4):
    n = int(input('Digite um num: '))
    s = s + n
print(f'Somatorio: {s} ')