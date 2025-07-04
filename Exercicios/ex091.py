# 4 jogadores jogam um dado
# randint
# guardar todo o resultado em um dicionario
# colocar em ordem, sabendo que o vencedor tirou o
# o maior numero no dado#
# saida = gera os numeros
# rankear os jogadores

from random import randint
# importando o random
resultados = {}
# inicia o dicionario de resultados


for c in range(4):
    resultados[f'Jogador {c+1}'] = randint(1,6)
# para c 4 vezes, coloque um randint no resultado

print('Valores: ')
for jogador, valor in resultados.items():
    print(f'{jogador} = {valor}')
# para cada jogador, valor nos items do dicionario :
# printa o jogador e o valor dele

ranking = []
# inicia o rankeamento em uma lista

for jogador, valor in resultados.items(): # para cada jogador, valor em items do dicionario
    inserido = False
    for i in range(len(ranking)): # para cada i no range do tamanho do ranking = 4
        if valor > ranking[i][1]: # se valor maior que o items na posicao i
            ranking.insert(i,(jogador,valor)) # entao insira no i, o jogador e seu valor
            inserido = True # inserido - verdaderio
            break
    if not inserido: # se nao inserido
        ranking.append((jogador,valor))
print(ranking) # printa o rankeadmento em formato lista, e items do dicionarios

for i,(jogador,valor) in enumerate(ranking, start=1): # para posicao i, o obejto jogador na posicao enumerada emm ranking comecando do 1
    print(f'{i} lugar: {jogador} com {valor}')

