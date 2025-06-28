# TUPLAS
"""
lanche = hamburguer  # variavel simples = lanche
lanche = suco    # apagou o hamburguer

variavel composto = tupla / listas / dicionario

# TUPLAS  == IMUTAVEIS - NAO CONSEGUE MUDAR
lanche =
() tupla = entre parentese
print(lanche[2])
"""

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') # criado tupla
# tupla sao imutaveis
# lanche[1] = 'Refri' #TypeError: 'tuple' object does not support item assignment

print(lanche)  # ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[2])  # Pizza
print(len(lanche))  # 4
print(lanche[2],':', len(lanche[2])) # Pizza : 5
print(lanche[-3]) # Suco
print(lanche[1:3]) #  ('Suco', 'Pizza') - do 1 ao 3, 3 - ignorado
print(lanche[2:]) # ('Pizza', 'Pudim') do 2 ate o final


for comida in lanche: # para cada comida em lanche
    print(f'Eu vou comer {comida}')  # vai printar cada item da tupla
print('Comi bem')

print(sorted(lanche)) # ['Hamburguer', 'Pizza', 'Pudim', 'Suco'] transformou em lista e ordebi

