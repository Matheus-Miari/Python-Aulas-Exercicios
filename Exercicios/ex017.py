"""
FACA UM PROGRAMA QUE LEIA O COMPRIMENRO DO CATETO
OPOSTO E DO CATETO ADJACENTE DE UM
TRIANGULO RETANGULO, CALCULE E MOSTRE
O COMPRIMENTO DA HIPOTENUSA
"""

from math import pow, sqrt

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
quadrado_hipotenusa = pow(ca,2) + pow(co,2)
hipotenusa = sqrt(quadrado_hipotenusa)

print(f'A hipotenusa deu: {hipotenusa:.2f}')

# math.hypot === hipotenusa no import math