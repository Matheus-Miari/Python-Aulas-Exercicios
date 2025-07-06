# FUNCAO CHAMADA CONTADOR()
# RECEBER 3 PARAMETROS
# INICIO, FIM E PASSO
# SAIDA:
# 1 ATE 10 DE 1 EM 1
# 10 TE 0 DE 2 EM 2
# CONTAGEM PERSONALIZADA
# #

from time import sleep
def contador(a,b,c):
    print('-'*20)
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    if a > b:
        cont = a
        while cont > b:
            print(a)
            a -= c
            cont -= c
            sleep(0.1)
    else:
        cont = a
        while cont <= b:
            print(a)
            a += c
            cont += c
            sleep(0.1)


#contador(1,10,1)
contador(1,10,1)
contador(10,0,2)
print( )
contador(a=int(input('Inicio: ')),
         b=int(input('Fim: ')),
         c=int(input('Passo: ')))
