#programa
# salario de um funcionrio com 15% de aumento
#
salario = float(input('Seu salario atual: R$'))
aumento = 0.15
novo_salario = salario + (salario * aumento)

print(f'Antes: R${salario:.2f}\nAumentou para: R${novo_salario:.2f}')