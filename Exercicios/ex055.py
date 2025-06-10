# ler o peso de 5 pessoas, no final mostrar
# qual foi o maior e o mneor peso
# lidos #

menor = 0
maior = 0

for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O menor peso foi {menor} kg')
print(f'O maior peso foi {maior} kg')
