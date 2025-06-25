# for variavel in range (valorInicial, valorFinal, [passo]):
#       condicao

soma = 0
N = int(input('Quantos numeros serao digitados:  '))

for i in range(0,N):
    x = int(input('Num: '))
    soma += x
print(f'Soma: {soma}')