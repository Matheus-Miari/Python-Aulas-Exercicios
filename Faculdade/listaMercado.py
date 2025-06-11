item = []    # inicia a lista vazia de items
mercado = []  # inicia a lista do MERCADO

for i in range(3):   # 3 items a serem add
    item.append(input('Digite o nome: '))   # add o nome do item
    item.append(input('Quantidade: '))  # add a quantidade
    item.append(float(input('Valor: ')))  # add o valor
    mercado.append(item[:]) # FAZ A COPIA DA LISTA E ADD NA LISTA DO MERCADO
    item.clear() # LIMPA O ITEM SE NAO VAI FICAR ADD
print(mercado)

mercadin = []
for i in range(3):
    nome = input('Nome: ')
    qtd = int(input('Quantidade: '))
    valor = float(input('Valor: '))
    mercadin.append([nome, qtd, valor])
print(mercadin)
