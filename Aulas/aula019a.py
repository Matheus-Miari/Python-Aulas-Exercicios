# dicionarios

dados = { # no dicionairo os indices sao as palavras chaves
    'nome': 'Matheus',
    'idade': 25
}

print(dados) #{'nome': 'Matheus', 'idade': 25}
print(dados['nome']) # Matheus
print(dados['idade']) # 25

dados['sexo'] = 'M'

print(dados) # {'nome': 'Matheus', 'idade': 25, 'sexo': 'M'}
del dados['idade'] # apaga o indice indicado
print(dados) # {'nome': 'Matheus', 'sexo': 'M'}

filme = {
    'titulo' : 'Star Wars',
    'ano' : '1977',
    'diretor': 'George Lucas'
}
print(filme) # {'titulo': 'Star Wars', 'ano': '1977', 'diretor': 'George Lucas'}
print(filme.values()) # dict_values(['Star Wars', '1977', 'George Lucas'])
print(filme.keys()) # dict_keys(['titulo', 'ano', 'diretor'])
print(filme.items()) # dict_items([('titulo', 'Star Wars'), ('ano', '1977'), ('diretor', 'George Lucas')])

for k, v in filme.items():
    print(f'O {k} = {v}')
    #O titulo = Star Wars
    #O ano = 1977
    #O diretor = George Lucas