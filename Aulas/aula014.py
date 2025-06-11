# estrutura de repeticao WHILE #
# WHILE = enquanto <condicao> faca:
#               instrucao
# while <condicao>:
#     instrucao
## c = 1
# while c < 11:
# print(c)
# c = c + 1
# print('Fim')
n = 1
par = 0
impar = 0
while n != 0:
     n = int(input('Digite um num: '))
     if n != 0:
         if n % 2 == 0:
             par += 1
         else:
            impar += 1
print('Fim')
print(f'Pares: {par}')
print(f'Impares: {impar}')