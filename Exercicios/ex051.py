# ler um termo e a razao de um PA
# NO FINAL mostre os 10 primeiros
# termos dessa progessao
# LER um termo e ir pulando de a cada razao#

i = int(input('Inicio: '))
p = int(input('PA: '))
decimo = i + ( 10 - 1 ) * p

for c in range  (i, decimo, p):
    print(f'{c}', end=' -> ')
print('Acabou')