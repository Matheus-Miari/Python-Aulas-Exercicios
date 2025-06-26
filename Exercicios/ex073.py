# criar uma tupla preenchida com os
# 20 primeiros colocados do brasileirao
# na ordem de colocacao
# mostre o 5 primeiros
# os ultimos 4
# uma lista com times em ordem alfabetica
# em que posicao esta O SP

tabela = (
    'Flamengo','Cruzeiro','Bragantino','Palmeiras','Bahia',
    'Fluminense','Atletico-MG','Botafogo','Mirassol','Corintia',
    'Gremio','Ceara','Vasco','Sao Paulo','Santos','Vitoria','Internacional',
    'Fortaleza','Juventude','Sport Recife'
)

# mostrar o 5 primeiros colocados
for time in tabela[0:5]:
    print(f'{tabela.index(time) + 1} - ', time)
#1 -  Flamengo
#2 -  Cruzeiro
#3 -  Bragantino
#4 -  Palmeiras
#5 -  Bahia

# mostrar os ultimos 4
print(f'{tabela[-4:]}')
# ('Internacional', 'Fortaleza', 'Juventude', 'Sport Recife')

# ordem alfabetica:
print(sorted(tabela))  # ordem alfabetica
# ['Atletico-MG', 'Bahia', 'Botafogo', 'Bragantino', 'Ceara', 'Corintia', 'Cruzeiro',
# 'Flamengo', 'Fluminense', 'Fortaleza', 'Gremio', 'Internacional',
# 'Juventude', 'Mirassol', 'Palmeiras', 'Santos',
# 'Sao Paulo', 'Sport Recife', 'Vasco', 'Vitoria']

# em que posicao esta ao SP
print(tabela.index('Sao Paulo')+1)
# 14