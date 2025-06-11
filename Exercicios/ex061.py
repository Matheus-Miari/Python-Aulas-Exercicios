# ler um termo e a razao de um PA
# MOSTRAR OS 10 primeiros termos
# da progressao com WHILE#

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 1  # Começa no primeiro termo

while contador <= 10:
    print(f'{termo} ', end='→ ')  # Mostra o termo
    termo += razao  # Calcula o próximo termo da PA
    contador += 1  # Atualiza o contador

print('FIM')