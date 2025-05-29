#programa que leia um numero e mostre sua tabuada
# #
import time

num1 = int(input('Numero: '))
print('-*-'*3)
for i in range(10):
    print(f'{num1} x {i:2} = {num1 * i}')
    time.sleep(0.3)
print('-*-'*3)