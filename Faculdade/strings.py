# manipulacao de strings

s1 = 'batatinha'
s1 = s1 + ' frita 1,2,3'

# print(s1)

s2 = 'B' + '='*20 + 'D'
# print(s2)

# composicao por marcador de posicao / concatenacao
# %d ou %i para numeros inteiros
# %f para numeros de ponto flutuantes
# %s para strings


nota = 8.5

s3 = 'Tu tirou %f na disciplina' %nota

print(s3)   # Tu tirou 8.500000 na disciplina

# %.2f limita a decimal

s4 = 'Tu tirou %.2f na disciplina' %nota

print(s4) #Tu tirou 8.50 na disciplina

disciplina = 'batatinha'

s5 = 'Tu tirou %.2f na %s' % (nota, disciplina)

print(s5) # Tu tirou 8.50 na batatinha

# COMPOSICAO MODERNA

# 'Tu tirou {} na disciplina'.format(nota)

s6 = 'Tu tirou {} na disciplina'.format(nota)

print(s6) # Tu tirou 8.5 na disciplina

# f - string = colocar f na frente da string e a variavel entre chaves

print(f'Voce tirou {nota} na disciplina de {disciplina}') # voce tirou 8.5 na disciplina de batatinha

