# ler nome, sexo e idade de varias pessoas
# guardar no dicionario
# todos os dicionarios em uma lista
# mostrar: quantas pessoas foram cadastradas
# a media de idade do grupo
# uma lista com todas as mulheres
# uma lista com pessoas com idade acima da MEDIA
# #
lista = []
dicionario = {}
lista_mulheres = []
lista_acima_idade = []
soma = media = 0
while True:
    dicionario['Nome'] = str(input('Nome: '))
    dicionario['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    if dicionario['Sexo'] == 'F':
        lista_mulheres.append(dicionario.copy()['Nome'])
    dicionario['Idade'] = int(input('Idade: '))
    if dicionario['Idade'] >= 18:
        lista_acima_idade.append(dicionario.copy()['Nome'])
    soma += dicionario['Idade']
    lista.append(dicionario.copy())
    resp = input('Quer continuar: ').upper()
    if resp == 'N':
        break
media = soma / len(dicionario)
print('-'*30)
print('Resultados')
print(f'Temos {len(lista)} pessoas cadastradas. ')
print(f'A media deu : {media:.2f}')
print('Mulheres: ')
for p in lista_mulheres:
    print(f'{p}')
print('Maiores: ')
for p in lista_acima_idade:
    print(f'{p}')