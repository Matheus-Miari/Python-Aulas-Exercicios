def soma(*num):
    acumulador = 0
    print(f'Tupla: {num}')
    for i in num:
        acumulador += i
    return acumulador

print(f'Resultado: {soma(1,2)}')
print(f'Resultado: {soma(1,2,3,4,5,6)}')

# Tupla: (1, 2)
# Resultado: 3
# Tupla: (1, 2, 3, 4, 5, 6)
# Resultado: 21 #