#programa que leia um numero inteiro qualquer e peca para o
# usuario escolher qual sera a base de conversao
# 1 para binario
# 2 para octal
# 3 para hexadecimal#

num = int(input('Digite um numero que deseja converter: '))
option = int(input('Deseja converter para qual base numerica: \n 1 - Binario \n 2 - Octal \n 3 - Hexadecimal '))

if option == 1:
    print(f'Binario: {bin(num)[2:]}')
elif option == 2:
    print(f'Octal: {oct(num)[2:]}')
elif option == 3:
    print(f'Hexadecimal: {hex(num)[2:]}')
else:
    print('Perdeu a chance')