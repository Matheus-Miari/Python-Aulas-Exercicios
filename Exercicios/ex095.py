jogadores = []

# Coleta de dados dos jogadores
while True:
    jogador = {}
    jogador['nome'] = input('Nome do jogador: ').strip()
    qtd_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    gols = []
    for partida in range(qtd_partidas):
        gols.append(int(input(f'  Quantos gols na partida {partida + 1}? ')))

    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())

    while True:
        resp = input('Deseja adicionar outro jogador? [S/N] ').strip().upper()
        if resp in ['S', 'N']:
            break
        print('Resposta inválida! Digite apenas S ou N.')

    if resp == 'N':
        break

# Mostrando um resumo geral dos jogadores
print('\n--- TABELA DE JOGADORES ---')
print(f'{"Cod":<4} {"Nome":<15} {"Gols":<20} {"Total":<5}')
print('-' * 50)
for idx, jogador in enumerate(jogadores):
    print(f'{idx:<4} {jogador["nome"]:<15} {str(jogador["gols"]):<20} {jogador["total"]:<5}')
print('-' * 50)

# Consulta de dados individuais
while True:
    busca = input('\nMostrar dados de qual jogador? (Digite o código ou "999" para sair): ')
    if not busca.isdigit():
        print('Por favor, digite um número válido.')
        continue

    busca = int(busca)
    if busca == 999:
        print('Finalizando...')
        break
    elif 0 <= busca < len(jogadores):
        jogador = jogadores[busca]
        print(f'-- LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
        for i, g in enumerate(jogador['gols']):
            print(f'   No jogo {i + 1} fez {g} gol(s)')
    else:
        print(f'Código inválido. Digite um número entre 0 e {len(jogadores) - 1} ou 999 para sair.')
