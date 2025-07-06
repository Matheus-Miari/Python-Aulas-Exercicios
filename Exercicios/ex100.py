# LISTA CHAMADA NUMEROS
# DUAS FUNCOES
# CHAMADAS SORTEIO E SOMAPAR
# A PRIMEIRA SORTEI 5 NUMEROS E COLOC DENTRO D LISTAA
# A SEGUNDA VAI MOSTRAR A SOMA DE TODOS OS PARES SORTEADOS #

from random import randint

lista_num = []

def sorteio(lst):  # define a funcao para receber um parametro
    for c in range(5): # para c 5 vezes
        lst.append(randint(1,10))# acrescenta um num aleatorio na lista
    print(f'Os nums sorteados foram: {lst}. ')


def somapar(lst):
    conta_pares = 0
    for c in lista_num:
        if c % 2 == 0:
            conta_pares += c
        else:
            continue
    print(f'A conta dos pares deu {conta_pares}. ')


sorteio(lista_num)
somapar(lista_num)







