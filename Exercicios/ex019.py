"""
FACA UM PROGRAMA QUE LEIA 4 NOMES
 E SORTEIE
"""
import random
print('--'*5 + 'SORTEIO' + '--'*5)

nome1 = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o ultimo nome: '))

nomes_array = [nome1,nome2,nome3,nome4]

sorteio = random.choice(nomes_array)

print(f'O ESCOLHIDO FOI....: {sorteio}')