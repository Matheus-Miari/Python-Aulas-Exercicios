"""
LER NOME DE 4 ALUNOS E SORTEIE
UMA ORDEM DE APRESENTACAO
"""
import random

nome1 = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o ultimo nome: '))

nomes_array = [nome1,nome2,nome3,nome4]
random.shuffle(nomes_array)

print(nomes_array)