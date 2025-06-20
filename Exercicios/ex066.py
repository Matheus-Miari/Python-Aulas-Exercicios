## um programa que leia varios numeros
# ineteiros, para quando digitr 999,
# quantos numeros foram digitados, e soma entre eles#

contador = 0
soma = 0

while True:
    numero = int(input('Digite um número (999 para parar): '))
    if numero == 999:
        break
    soma += numero
    contador += 1

print(f'Você digitou {contador} números e a soma entre eles é {soma}.')
