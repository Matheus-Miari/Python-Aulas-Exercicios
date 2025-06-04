#ler um valor a ser pago por um produto
# considerando o seu preco normal
# e condicao de pagamento
# a vista dinheiro= 10% de desconto
# vista cartao = 5%
# 2x no cartao = preco normal
# 3x ou mais 20% de juros#

valor_produto = float(input('Qual o valor do produto: '))
idPagamento = int(input('Deseja pagar de qual forma:\n 1: A VISTA DINHEIRO \n 2: A VISTA CARTAO \n 3: 2x NO CARTAO \n 4: 3x NO CARTAO '))

if idPagamento == 1:
    print(f'Vai pagar um total de R$ {valor_produto - valor_produto * 10 / 100:.2f}')
elif idPagamento == 2:
    print(f'Vai pagar um total de R$ {valor_produto - valor_produto * 5 / 100:.2f}')
elif idPagamento == 3:
    print(f'Vai pagar um total de R$ {valor_produto:.2f}')
elif idPagamento == 4:
    print(f'Vai pagar um total de R$ {valor_produto + valor_produto * 20 / 100:.2f}')