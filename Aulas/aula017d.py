a = [2,4,5,6]
b = a  # cria uma ligacao / conexao com a lista  a, nao uma copia
b[2] = 10  # [2, 4, 10, 6] nas duas listas
print(a)
print(b)

c = a[:]  # assim se cria uma copia
c[1] = 3
print(c) # [2, 3, 10, 6]