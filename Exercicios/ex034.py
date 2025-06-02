"""
LER UM SALARIO E DAR UM AUMENTO
PARA SALARIOS MAIORES QUE 1250 AUMENTA 10 %
PRA INFERIOES OU IGUAIS AUMENTO DE 15%
"""

salario = float(input('Qual seu salario: '))
if salario > 1250:
    print(f'Seu salario foi de R${salario:.2f} para R${salario + (salario * 10 / 100):.2f}')
else:
    print(f'Seu salario foi de R${salario:.2f} para R${salario + (salario * 15 / 100):.2f}')