# tabuada de um numero que o usuario escolher#
from time import sleep

num = int(input('Tabuada de qual numero: '))
for c in range(0,11):
    print(f'{num} x {c} = {num * c}')
    sleep(0.3)
print('Prontinho...')