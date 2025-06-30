# UM APP DE VENDAS = MARMITAS
#  BA - FF
# P - M - G
# tamanho_linha = xx, linha = tamanho_linha - len(palavra)
# Cardapio = 8 caracter e a linha vai ter 50, ai vc save que tera que colocar 42 "-"

titulo = "BEM-VINDO A MARMITARIA DO MATHEUS MIARI"
print('-'+len(titulo)*'-')
print('-'+titulo+'-')
cardapio = 'Cardápio'
print('-'*len(cardapio)*2 + cardapio+ '-'*len(cardapio)*2)
print('---| Tamanho | Bife Acebolado (BA) | File de frango (FF) |---')
print('---|    P    |       R$ 16.00      |     R$ 15.00        |---')
print('---|    M    |       R$ 18.00      |     R$ 17.00        |---')
print('---|    G    |       R$22.00       |     R$ 21.00        |---')
print('--'*20)

valorTotal = 0
opcao = 999

while opcao not in ['N']:
    sabor = str(input('Entre com o sabor desejado (BA/FF): ')).upper().strip()
    while sabor not in ['BA', 'FF']:
        sabor = str(input('Sabor inválido. Tente novamente: '))
        continue
    tamanho = str(input('Entre com o tamanho desejado (P/M/G): ')).upper().strip()[0]
    while tamanho not in ['P', 'M', 'G']:
        tamanho = str(input('Tamanho invalido. Tente novamente: '))
        continue

    if sabor == 'BA':
        if tamanho == 'P':
            valorTotal += 16
        elif tamanho == 'M':
            valorTotal += 18
        elif  tamanho == 'G':
            valorTotal += 22
    elif sabor == 'FF':
        if tamanho == 'P':
            valorTotal += 15
        elif tamanho == 'M':
            valorTotal += 17
        elif tamanho == 'G':
            valorTotal += 21

    print(f'Você pediu um {sabor} no tamanho {tamanho}: R${valorTotal:.2f}')
    opcao = str(input('Deseja mais alguma coisa?')).upper().strip()
    if opcao == 'N':
        break

print(f'O valot total a ser pago: R${valorTotal:.2f}')
