#TABUDA DE VARIOS NUMEROS
# UM DE CADA VEZ, PARA CADA VALOR, DIGITADO
# INTERROMPE SE FOR NEGATIVO

while True:
    numero = int(input('Digite um número para ver a tabuada (negativo para sair): '))
    if numero < 0:
        break
    print('-' * 30)
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
    print('-' * 30)
print('Programa encerrado. Obrigado!')