# criar uma matriz de 3x3 para preencher
# no final, mostrar a matriz na tela, com a formatacao correta#

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Valor na [{i},{j}]: ' ))
        linha.append(valor)
    matriz.append(linha)

print(f'Matriz digitada: ')
for l in matriz:
    for num in l:
        print(f'[{num}]', end=' ')
    print()
