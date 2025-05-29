# Escreva um programa que pergunte a quantidade de Km percorridos por
# um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quanto km tu rodou: '))
dias = int(input('Quantos dias o carro foi alugado: '))

em_dias = 60 * dias
em_km = km * 0.15

total = em_km + em_dias

print(f'Em Km vc gastou R${em_km:.2f}')
print(f'Em dias deu R${em_dias:.2f}')
print(f'A conta total deu R${total:.2f}')
