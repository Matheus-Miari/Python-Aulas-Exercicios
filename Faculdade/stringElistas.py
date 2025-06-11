#
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
# indices =    0          1        2         3

# cada item dentro na lista tbm tem seu proprio indice
# COMO ACESSAR

print(mochila[0][0])  # M == PQ ACESSOU O INDICE 0 DA LISTA E DPS O INDICE DO ITEM -- MACHADO == M

# DUPLA INDEXACAO

for item in mochila:
    for letra in item:
        print(letra,end='-')
    print() # QUEBRA DE LINHA
    # RESULTADO
    # M-a-c-h-a-d-o-
    # C-a-m-i-s-a-
    # B-a-c-o-n-
    # A-b-a-c-a-t-e-

mala = [['Cebola', 0.39], ['Tomate', 0.49], ['Batata', 0.89]] # lista dentro de lista
#indices =    0                1                      2
# i x 2 - 0       1          0        1        0          1



