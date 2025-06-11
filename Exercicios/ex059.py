# ler dois valores
# e mostrar um menu na tela
# 1 para somar
# 2 multiplicar
# 3 maior
# 4 novos numeros
# 5 sair #

n1 = int(input('Digite o primeiro num: '))
n2 = int(input('Digite o segundo num: '))
resp = 0
while resp != 5:
    resp = int(input('--Menu-- \n 1 - SOMAR \n 2 - MULTIPLICAR \n 3 - Maior entre eles \n 4 - Digitar novos numeros \n 5 - Sair \n'))
    if resp == 1:
        print(f'Soma de {n1} + {n2} = {n1 + n2}')
        break
    elif resp == 2:
        print(f'Multiplicacao de {n1} * {n2} = {n1 * n2}')
        break
    elif resp == 3:
        print(f'O maior entre {n1} e {n2} = {max(n1,n2)}')
        break
    elif resp == 4:
        n1 = int(input('Digite o primeiro num: '))
        n2 = int(input('Digite o segundo num: '))
    elif resp == 5:
        break
    else:
        print('Opcao invalida')