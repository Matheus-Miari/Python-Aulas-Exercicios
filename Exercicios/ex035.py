"""
LER 3 RETAS  E DIZER SE PODE OU NAO
FORMAR UM TRIANGULO
*PRINCIPIO MATEMATICO
"""

r1 = float(input('Primeiro valor: '))
r2 = float(input('Segundo valor: '))
r3 = float(input('Terceiro valor: '))

if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print('Nao pode formar um triangulo')
else:
    print('Podem formar um triangulo')