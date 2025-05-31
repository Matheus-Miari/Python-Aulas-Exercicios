# LEIA UMA FRASE E MOSTRE
# QUANTAS VEZES APARECE O A
# EM QUE POSICAO ELA APARECE PELA PRIMEIRA VEZ
# POSICAO QUE APARECE PELA ULTIMA VEZ#

frase = str(input('Digite uma frase: '))
qtd_a = frase.count('a')
idx_a = frase.find('a')
ult_a = frase.find('a')

print(f'{qtd_a}, {idx_a}, {ult_a}')