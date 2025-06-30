# ler varios numeros e colocar em uma lista
# mostrar quantos numeros forao digitados
# a lista em ordem decrescente
# se o 5 foi digitado

lista = []

while True:
    num = int(input('Digite um num (999 para sair): '))
    if num == 999:
        break
    else:
        lista.append(num)
cont = 0

for valor in lista:
    if valor == 5:
        cont += 1

print(f'Lista: {lista}')
lista_de = sorted(lista, reverse=True)
print(f'Lista decrescente: {lista_de}')
print(f'O 5 foi digitado {cont} vezes.')
