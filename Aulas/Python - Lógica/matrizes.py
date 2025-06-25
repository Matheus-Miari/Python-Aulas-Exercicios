# minha_matriz = [[0 for x in range(numero_de_colunas)] for x in range(numeroDeLinhas)]

M = int(input('Qtd de linhas: '))
N = int(input('Qtd de colunas: '))

mat = [[0 for x in range(N)] for x in range(M)]  # primeiro colunas dps linhas

#logica para correr

for i in range(0,M):
    for j in range(0,N):
        mat[i][j] = int(input(f'Elemento [{i},{j}]: '))

print()
print('Matriz digitada')
for i in range(0,M):
    for j in range(0,N):
        print(f"{mat[i][j]} ", end="")
    print()