print('--Boas-Vindas--')
print('Desenvolvido por Matheus Miari')

valorDaParcela = 0
valorDoPedido = 0
quantidadeParcelas = 0
valorTotalParcelado = 0

valorDoPedido = float(input('Digite o valor do pedido em R$: '))   # solicitando o valor do pedido
quantidadeParcelas = int(input('Digita quantidade de parcelas: '))

if quantidadeParcelas < 4:   # condicao de teste de quantidade de parcelas
    juros = 0 / 100
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6 : # testa se a quantidade de parcelas esta entre 4 e 6
    juros = 4 / 100
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9: # testa se a quantidade de parcelas esta entre 6 e 9
    juros = 8 /100
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13: # testa se a quantidade de parcelas esta entre 9 e 13
    juros = 16 / 100
else: # cai diretamente em 32% de juros
    juros = 32 / 100

valorDaParcela = valorDoPedido * (1 + juros) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

print(f'Valor total do pedido: R${valorDoPedido} \nQuantidade de parcelas: {quantidadeParcelas} \nValor da parcela:R${valorDaParcela:.2f} \nValor Total Parcelado: R${valorTotalParcelado}')

