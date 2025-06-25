# estrutura condicional

# if condicao :
#    comando indantado

x = int(input('Que horas sao: '))

if x <= 12 :
    print(f'Bom dia ')
elif x > 12 and x < 18:   # CONDICAO INTERMEDIARIA 
    print(f'Boa tarde ')
else:
    print(f'Boa noite ')