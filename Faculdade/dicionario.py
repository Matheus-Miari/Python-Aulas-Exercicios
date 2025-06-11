# estrutura de dados dinamica
# pode alterar dados e tamanho == mutaveis
# indexados por palavras chaves
#  {} #
# palavra-chave:dado

mochila = {'Note':1, 'Celular':2, 'PowerBank':3, 'Carregador':4}
print(f'Dicionario: {mochila}') # Dicionario: {'Note': 1, 'Celular': 2, 'PowerBank': 3, 'Carregador': 4}

game = {'Nome':'GoW',
        'Desen':'Nintendo',  # sempre em pares
        'Ano':1990}
print(game)  # {'Nome': 'GoW', 'Desen': 'Nintendo', 'Ano': 1990}

print(game['Nome'])  # acessa pela palavra chave = GoW
print(game['Desen']) # Nintendo
print(game['Ano']) # 1990

