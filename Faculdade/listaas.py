# listas
# podem alterar dados e tamanho == MUTAVEIS
# indexadas por valores numericos inteiros
# representados em python por colchetes [  ]
# #

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(f'LISTA: {mochila}')  # LISTA: ['Machado', 'Camisa', 'Bacon', 'Abacate']

mochila[2] = 'Laranja' ## nao da erro pois listas sao mutaveis
print(mochila)  # ['Machado', 'Camisa', 'Laranja', 'Abacate']

mochila.append('Ovos') # add no final da lista
print(f'APPEND:{mochila}') # APPEND:['Machado', 'Camisa', 'Laranja', 'Abacate', 'Ovos']

mochila.insert(1, 'Canivete') # insere na posicao informada
print(f'Inset: {mochila}') # Inset: ['Machado', 'Canivete', 'Camisa', 'Laranja', 'Abacate', 'Ovos']

mochila.remove('Ovos') # deleta o dado informado
print(f'Removi o ovo: {mochila}') # Removi o ovo: ['Machado', 'Canivete', 'Camisa', 'Laranja', 'Abacate']

del mochila[1] # deleta o indice informado
print(f'Removido indice 1: {mochila}') # Removido indice 1: ['Machado', 'Camisa', 'Laranja', 'Abacate']

