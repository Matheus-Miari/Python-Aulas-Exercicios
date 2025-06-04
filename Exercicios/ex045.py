# programa que jogue pedra papel e tesoura
#

import random

user = int(input('1 - pedra \n 2 - tesoura \n 3 - papel: '))
computer = random.randint(1,3)
print(f'Escolhi {computer} e vc {user}')
if user == computer:
    print('MESMA COISA')
elif user == 1 and computer == 3:
    print('GANHOU')
elif user == 2 and computer == 3:
    print('GANHOU')
elif user == 3 and computer == 1:
    print('GANHOU')
else:
    print('PERDI')