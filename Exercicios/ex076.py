# tupla com nomes de produtos
# seus precos
# mostrar uma listagem de precos organizndo
# os dados em forma tabular

tupla = (
    'Lapis', 1.75,
    'Borracha', 14.30,
    'Estojo', 15.00,
    'Mochila', 13.22,
    'Tenis', 14.33,
    'Livro', 34.90
)
print('-'*40)
print(f'{"LISTA":^40}')
print('-'*40)
for item in range(0, len(tupla)):
    if item % 2 == 0:
        print(f'{tupla[item]:.<30}', end='')
    else:
        print(f'R${tupla[item]:>6.2f}')
print('-'*40)