# Faca um programa ue leia algo pelo teclado e
# mostre na tela o seu tiop primitivo e todas
# as informacoes positives sobre ele:
# num, alpha, alphanumeric

from curses.ascii import isalpha

algo = input('Digite qualquer coisa cabron: ')
print(f'O tipo primitivo deste valor: {type(algo)}')
print(f'Alpha: {algo.isalpha()}')
print(f'Num: {algo.isnumeric()}')
print(f'Alphanumerico: {algo.isalnum()}')
print(f'So espaco: {algo.isspace()}')
print(f'Maiusculas: {algo.isupper()}')
print(f'Minusculas: {algo.islower()}')
print(f'Capitalizada: {algo.istitle()}')