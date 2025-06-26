# LER 4 NUMEROS
# GUARDAR NA TUPLA
# QUANTAS VEZES O 9 APARECE
# EM QUE POSICAO ESTA O PRIMEIRO 3
# QUAIS SAO PARES

tupla_num = (int(input('Digite um num: ')),
             int(input('Digite um num: ')),
             int(input('Digite um num: ')),
             int(input('Digite um num: ')),)

print(tupla_num)

# numero 9
print(f'O valor 9 apareceu {tupla_num.count(9)} vezes.')
if 3 in tupla_num:
    print(f'O num 3 apareceu na {tupla_num.index(3)+1} posicao')
else:
    print('Valor 3 nao encontrado')

print('Pares: ')
for n in tupla_num:
    if n % 2 == 0:
        print(n, end=' ')