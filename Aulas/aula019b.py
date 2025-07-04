pessoas = {
    'nome':"Matheus",
    'sexo' : 'M',
    'idade': '25'
}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos. ')
# O Matheus tem 25 anos.
print(pessoas.keys())
# dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values())
# dict_values(['Matheus', 'M', '25'])
print(pessoas.items())
# dict_items([('nome', 'Matheus'), ('sexo', 'M'), ('idade', '25')])
for k in pessoas.keys():
    print(k)
    #nome
    #sexo
    #idade
del pessoas['sexo'] # apaga a key sexo
print(pessoas)
# {'nome': 'Matheus', 'idade': '25'}

pessoas['nome'] = 'Batata' # trocando nome por batata
print(pessoas)
# {'nome': 'Batata', 'idade': '25'}

pessoas['peso'] = '66'
print(pessoas)
# {'nome': 'Batata', 'idade': '25', 'peso': '66'}