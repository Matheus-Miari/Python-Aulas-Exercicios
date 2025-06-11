# TUPLA
# ESTRUTURA DE DADOS  ESTATICA
# TUPLA = = IMUTAVEL
# REPRESENTADA POR ( )  #

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')  # tupla

print(mochila)

print(mochila[0])   # indice 0 == machado
print(mochila[2])   # indice 2 == BACON
print(mochila[0:2])   # indice 0 E 1 == ('Machado', 'Camisa')
print(mochila[2:])   # A PARTIR DO INDICE 2 == ('Bacon', 'Abacate')
print(mochila[-1])   # ULTIMO ELEMENTO == Abacate

# se tentar
# mochila[2] = 'OVOS' VAI DAR ERRO, POIS A TUPLA == IMUTAVEL

for item in mochila:
    print(f'Na minha mochila tem: {item}')
    # Na minha mochila tem: Machado
    # Na minha mochila tem: Camisa
    # Na minha mochila tem: Bacon
    # Na minha mochila tem: Abacate

