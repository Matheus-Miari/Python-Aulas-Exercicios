"""
LER UM ANO QUALQUER E DIZER
SE ELE E BISSEXTO
"""
from datetime import date

ano = int(input('Qual ano tu quer saber: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano de {ano} BISSEXTO')
else:
    print(f'O ano de {ano } NAO E BISSEXTO')