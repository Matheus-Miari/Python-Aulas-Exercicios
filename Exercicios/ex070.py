# ler o nome e preco de varios produtos
# o programa pergunta se quer continuar
# total gasto
# quantos produtos custam mis de 1000
# nome do produtaa mais barato#

total_gasto = 0
produtos_caros = 0
menor_preco = 0
produto_mais_barato = ''
contador = 0

while True:
    print('-' * 30)
    print('CADASTRE UM PRODUTO')
    print('-' * 30)

    nome = input('Nome do produto: ').strip()
    preco = float(input('Preço: R$'))

    total_gasto += preco
    contador += 1

    if preco > 1000:
        produtos_caros += 1

    if contador == 1 or preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = nome

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()

    if continuar == 'N':
        break

print('-' * 30)
print(f'Total gasto na compra: R${total_gasto:.2f}')
print(f'Quantidade de produtos que custam mais de R$1000: {produtos_caros}')
print(f'O produto mais barato foi "{produto_mais_barato}" que custa R${menor_preco:.2f}')
print('FIM DO PROGRAMA')