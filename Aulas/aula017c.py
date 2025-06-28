valores = []
valores.append(5)
valores.append(9)
valores.append(3)
lista = []

print('Os valores sao: ')
for valor in valores:
    print(f'{valor}..', end='') # 5..9..3..

print(' ')
for c, v in enumerate(valores):
    print(f'Na pos {c}, o valor: {v}')
    # Na pos 0, o valor: 5
    # Na pos 1, o valor: 9
    # Na pos 2, o valor: 3
print('Fim..')

for cont in range(0,5):
    lista.append(int(input('Digite um num: ')))

print(lista)