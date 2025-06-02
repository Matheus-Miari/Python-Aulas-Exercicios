# LEIA UMA FRASE E MOSTRE
# QUANTAS VEZES APARECE O A
# EM QUE POSICAO ELA APARECE PELA PRIMEIRA VEZ
# POSICAO QUE APARECE PELA ULTIMA VEZ#

frase = str(input('Digite uma frase: ')).upper().strip()
qtd_a = frase.count('A')
idx_a = frase.find('A') + 1
ult_a = frase.rfind('A') + 1

print(f'{qtd_a}, {idx_a}, {ult_a}')