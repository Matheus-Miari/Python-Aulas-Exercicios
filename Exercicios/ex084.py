# ler nome e peso pessoa de varias pessoas
# mostrar: quantas pessoas
# foram cadastradas
# listagem de pessoas mais pesadas
# lista com pessoas mais leves#

pessoa= list()
maisPesada = list()
maisLeve = []
maiorPeso = menoPeso = 0

print('-='*30)
print('Vc vai digitar nome e peso (Digite N para sair)')
print('-='*30)

while True:
    nome = input('Nome: ').upper()
    if nome == 'N':
        break
    peso = float(input('Peso: '))
    pessoa.append([nome,peso])

    if len(pessoa) == 1:
        maiorPeso = menoPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menoPeso:
            menoPeso = peso

    resp = input('Quer continuar? [S/N]: ').strip().upper()
    if resp == 'N':
        break

for p in pessoa:
    if p[1] == maiorPeso:
        maisPesada.append(p[0])
    if p[1] == menoPeso:
        maisLeve.append(p[0])

print('-=' * 30)
print(f'Ao todo foram cadastradas {len(pessoa)} pessoas.')
print(f'O maior peso foi {maiorPeso}kg. Peso de: {maisPesada}')
print(f'O menor peso foi {menoPeso}kg. Peso de: {maisLeve}')