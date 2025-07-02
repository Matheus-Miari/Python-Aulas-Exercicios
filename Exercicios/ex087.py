# aprimorar a matriz
# som de todos os pares
# soma da terceira coluna
# o maior valor da segunda linhas#

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Valor na [{i},{j}]: ' ))
        linha.append(valor)
    matriz.append(linha)

somaDaColuna = sum(linha[2] for linha in matriz)
maiorValor = max(matriz[1])

# SAIDA
print(f'Matriz digitada: ')
for l in matriz:
    for num in l:
        print(f'[{num}]', end=' ')
    print()

print(f'Soma da terceira coluna: {somaDaColuna}')

for linha in matriz:
    print(f'{linha[2]}', end='...')

print()
print(f'Maior valor da segunda linha: {maiorValor}')

print(matriz)