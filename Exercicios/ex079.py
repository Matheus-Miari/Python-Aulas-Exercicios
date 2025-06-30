# ler valores varios valores numericos
# colocar numa lista, caso o numero ja estiver na lista
# o numero nao sera adicionado
# mostrar os valores e ordem crescente

lista = []

while True:
    num = int(input('Digite um num: '))
    if num < 0:
        break
    elif num not in lista:
        lista.append(num)
    elif num in lista:
        print(f'Num {num} ja esta na lista.')

print(f'Lista : {lista}')
print(f'Ordem crescente: {sorted(lista)}')