# ler 3 retas, dizer se forma um triangulo
# se formar triangulo dizer qual e
# equilatero = todos os lados iguais
# isosceles = dois lados iguais
# escaleno = todos os lados difernetes#
from time import sleep

r1 = int(input('Primeira reta: '))
r2 = int(input('Segunda reta: '))
r3 = int(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Podem formar um triangulo')
    print('Agora vou analisar qual tipo de triangulo...')
    sleep(2)
    if r1 == r2 == r3:
        print('Triangulo equilatero pois todos os lados sao iguais')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2:
        print('ISOSCELES')
    else:
        print('ESCALENO')
else:
    print('NAO PODEM FORMAR UM TRIANGULO')