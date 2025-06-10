"""
FACA UM PROGRAMA QUE LEITA UM ANGULO QUALQUER
E MOSTRE NA TELA O VALOR DE SENO, COSSENO E TANGENTE
DESSE ANGULO
"""
import math

print('--'*10)
angulo = math.radians(float(input('Digite o angulo: ')))

seno_angulo = math.sinh(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f'Seno = {seno_angulo:.2f}\nCosseno = {cosseno:.2f}\nTangente = {tangente:.2f}')

