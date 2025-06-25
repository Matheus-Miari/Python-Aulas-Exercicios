# vetores


# nome_vetor = [0 for x in range(numero_de_elementos)]

N = int(input('Quantos numeros voce vai digitar: '))
vet = [0 for x in range(N)]

for i  in range(0,N):
    vet[i] = float(input('Digite o num: '))

print()
print('Numeros digitados: ')

for i in range(0,N):
    print(f'Vet = {vet[i]:.1f}')