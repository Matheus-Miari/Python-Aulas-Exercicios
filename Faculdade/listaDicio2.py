games = {'Nome':[],'VideoGame':[],'Ano':[]}

for i in range(3):
    nome = input(f'Digite o nome do {i + 1}º jogo: ')
    videogame = input(f'Digite o videogame do {i + 1}º jogo: ')
    ano = int(input(f'Digite o ano de lançamento do {i + 1}º jogo: '))

    games['Nome'].append(nome)
    games['VideoGame'].append(videogame)
    games['Ano'].append(ano)
print(games)