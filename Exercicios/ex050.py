# programa que leia seis numeros inteiros
# e mostre a soma apneas daquele que forem pares
# se o valor digitado for impar, desconsiderar#

soma = 0

for c in range(0,6):
    num = int(input('Digite um num: '))
    if num % 2 == 0:
        soma = soma + num
print(f'O somatorio dos valores pares digitados foi {soma}')
