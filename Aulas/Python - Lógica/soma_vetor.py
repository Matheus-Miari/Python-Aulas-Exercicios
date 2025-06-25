N = int(input('Quantos nums vai digitar: '))

vet =  [0 for x in range(N)]

for i in range(0,N):
    vet[i] = float(input('Num: '))

print()
print(f'Valores = ', end='')

for i in range(0,N):
    print(f'{vet[i]:.1f} ', end='')

print()

soma = 0

for i in range(0,N):
    soma += vet[i]

print(f'Soma: {soma}')

media = soma / N

print(f'Media: {media:.2f}')