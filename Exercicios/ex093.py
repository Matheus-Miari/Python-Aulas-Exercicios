# gerenciar um aproveitamento de um jogador de futebol
# o programa vai ler o nome do jogador
# quantas partidas ele jogou
# depois vai ler a quantidade de gols
# feitos em cada partida
# no final tudo isso sera guardao em um dicionario
# incluido o total de gols feitos
# saida = nome, qtd partidas, quantos gols em cada partida
# #

jogadores = [] # inicia a lista de jogadores
qtd_Partidas = 0 # quantidade de partidas
while True:
    # enquanto verdade
    jogador = {}  # inicia o dicionario
    jogador['nome'] = str(input('Nome: '))
    jogador['qtdPartidas'] = int(input('Quantas partidas: '))
    qtd_Partidas = jogador['qtdPartidas']
    gols = [] # inicia a lista de gols
    for c in range(qtd_Partidas):  # para c em qtd de paritdas, para pedir quantos gols por partida
        gols.append(int(input(f'Gols na {c+1} partida: ')))   # gols add na lista em ordem
    jogador['gols'] = gols # add a lista de gols no dicionario
    jogador['total'] = sum(gols) # add o total de gols no dicionairo
    jogadores.append(jogador.copy())  # copia o jogador sem sobrescrever

    resp = input('Quer continuar: ').upper()
    if resp == 'N':
        break

for i, jogador in enumerate(jogadores):  # para posicao, jogador em enumerate jogadores
    print(f'Jogador {i + 1}:')  # posicao i + 1
    print(f'  Nome: {jogador["nome"]}')  # printa o nome do jogador
    for i_partida, gol in enumerate(jogador['gols']):  # cada prtida no dicionario na lista gols
        print(f'    Partida {i_partida + 1}: {gol} gol(s)')
    print(f'  Total de gols: {jogador["total"]}')
    print('-' * 10)
