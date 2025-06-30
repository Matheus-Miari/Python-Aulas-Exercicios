galera = list()

dado = list()

for c in range(0,3):
    dado.append(str(input(f'Nome da {c+1} pessoa: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # copia do dado
    dado.clear()

print(galera) # Idade: 44 [['primeira', 11], ['segybnda', 23], ['terceira', 44]]


for p in galera:
    if p[1] >= 21:
        print(f'O {p[0]} - maior de idade')