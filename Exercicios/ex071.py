# caixxa eletronico
# qual valor a ser sacado = int
# quntas ceduls sero utilizdas
# #

print('==== CAIXA ELETRÔNICO ====')
valor = int(input('Qual valor você deseja sacar? R$ '))
cedulas = [100, 50, 20, 10, 5, 2]
resultado = {}

for cedula in cedulas:
    if valor >= cedula:
        quantidade = valor // cedula
        valor = valor % cedula
        resultado[cedula] = quantidade

print('\nCédulas fornecidas:')
for cedula, quantidade in resultado.items():
    print(f'{quantidade} cédula(s) de R$ {cedula}')

if valor != 0:
    print(f'Não foi possível sacar R$ {valor} (valor restante).')

print('==== FIM ====')