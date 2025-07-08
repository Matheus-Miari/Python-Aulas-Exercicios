from time import sleep


def contador(i,f,p): # criar manual
    """
    -> Faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        sleep(0.5)
        c += p
    print('Fim')


# contador(2,10,2)

help(contador)
#contador(i, f, p)
# -> Faz uma contagem e mostra na tela
#     :param i: Inicio da contagem
#     :param f: Fim da contagem
#     :param p: Passo da contagem
#     :return: sem retorno#