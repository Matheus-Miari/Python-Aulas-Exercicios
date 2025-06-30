# varios numeros em uma lista
# duas lista para pares e impares

lista = []
listaPares = []
listaImpares = []
while True:
    num = int(input('Digite um num (999 para parar): '))
    if num == 999:
        break
    else:
        lista.append(num)

for valor in lista:
    if valor % 2 == 0:
        listaPares.append(valor)
    else:
        listaImpares.append(valor)

print(f'Lista: {lista}')
print(f'Lista ordenada: {sorted(lista)}')
print(f'Lista Pares: {listaPares}')
print(f'Lista Impares: {listaImpares}')