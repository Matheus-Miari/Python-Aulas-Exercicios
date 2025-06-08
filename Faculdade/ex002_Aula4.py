# escreva um programa que leia um valor e que
# imprima a qunaitade de cedulas necessarias
#  para pagar esse mesmo valor#
from time import sleep

valor = int(input("Digite um valor em reais: R$ "))

cedulas = [100, 50, 20, 10, 5, 2, 1]

print(f"Para pagar R$ {valor}, será necessário:")

for cedula in cedulas:
    quantidade = valor // cedula
    if quantidade > 0:
        print(f"{quantidade} cédula(s) de R$ {cedula}")
        valor = valor % cedula
