# desafio 61 com a opcao de mostrar mais termos definidos
# por usuario#

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

contador = 1
total_termos = 10
mais_termos = 10

while mais_termos != 0:
    while contador <= total_termos:
        print(f'{termo} ', end='→ ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos a mais você quer mostrar? '))
    total_termos += mais_termos

print('FIM DA PROGRESSÃO')
