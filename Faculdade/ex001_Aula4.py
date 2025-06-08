# escreva um algoritmo que mostre na tela quatro
# produtos a serem comprados em uma lanchonete
# #

print('1: Coxinha - R$ 15,00')
print('2: Pastel - R$ 7,00')
print('3: Cafe - R$ 4,00')
print('4: Suco - R$ 6,00')
print('5: SAIR')
total = 0
while True:
    op = float(input('Qual item vai cobrar: '))
    qtd = int(input('Quantidade: '))

    if (op == 1):
        total += qtd * 15.00
    elif (op == 2):
        total += qtd * 7.00
    elif (op == 3):
        total += qtd * 4.00
    elif (op == 4):
        total += qtd * 6.00
    else:
        print('Saindo...')
        break
print(f'Total: R$ {total:.2f}')