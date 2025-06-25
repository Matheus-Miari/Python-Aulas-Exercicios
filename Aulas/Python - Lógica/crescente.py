print('Digite dois numeros: ')
x = int(input())
y = int(input())

while x != y:
    if x < y:
        print('Crescente')
    else:
        print('Decrescente')
    print('Outros dois nums: ')
    x = int(input())
    y = int(input())
print('Encerrando...')