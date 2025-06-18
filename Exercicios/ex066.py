## um programa que leia varios numeros
# ineteiros, para quando digitr 999,
# quantos numeros foram digitados, e soma entre eles#


soma = 0
cont = 0
while True:
        n = int(input('Digite um num: '))
        if n == 999:
            break
        soma += n
        cont += 1
print(f'Som: {soma} \nContagem: {cont}')