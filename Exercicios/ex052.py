# numero inteiro e dizer se e primo#

num = int(input('Digite um número: '))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print('NÃO PRIMO')
            break
    else:
        print('PRIMO')
else:
    print('NÃO PRIMO')
