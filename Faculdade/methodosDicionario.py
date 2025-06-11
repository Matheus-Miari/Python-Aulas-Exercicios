# values = obtem somente os dados
# keys = obtem somente as chaves
# items = obtem o par chave:dado #

game = {'Nome':'GoW',
        'Desen':'Nintendo',  # sempre em pares
        'Ano':1990}

print(game.values())  # dict_values(['GoW', 'Nintendo', 1990])
for values in game.values():
    print(values) # GoW Nintendo 1990 #

print(game.keys()) # dict_keys(['Nome', 'Desen', 'Ano'])
for keys in game.keys():
    print(keys)
# Nome
# Desen
# Ano #

print(game.items())  # dict_items([('Nome', 'GoW'), ('Desen', 'Nintendo'), ('Ano', 1990)])
for keys, values in game.items():
    print(f'{keys} = {values}')
# Nome = GoW
# Desen = Nintendo
# Ano = 1990 #

