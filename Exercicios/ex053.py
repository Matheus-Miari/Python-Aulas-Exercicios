# ler um programa que leia uma frase qualquer
# e dizer se ela e um palindromo desconsiderando
# os espacos ler de tras pra frente #
from os.path import split

frase = str(input('Digite um frase: ')).strip().upper()
frase_semEspaco = ''.join(frase.split())

if frase_semEspaco == frase_semEspaco[::-1]:
    print('Palindromo')
else:
    print('Nao e palindromo')