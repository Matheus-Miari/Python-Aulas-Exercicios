jogadores = [] # inicia a lista de jgoadores

# Coleta de dados dos jogadores
while True: # laco infinito enquanto verdade
    jogador = {} # dict jogador inicia toda vez que comeca o laco
    jogador['nome'] = input('Nome do jogador: ').strip()
    qtd_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = [] # lista de gols que vai ser colocada no dicionario do jgoador
    for partida in range(qtd_partidas): # para cada partida em quantidade de partidaa
        gols.append(int(input(f'  Quantos gols na partida {partida + 1}? '))) # gols recebe a quantidade de gols
    jogador['gols'] = gols  # linkado gols no jogador
    jogador['total'] = sum(gols) # soma total
    jogadores.append(jogador.copy()) # dict jogador copia
    while True:
        resp = input('Deseja adicionar outro jogador? [S/N] ').strip().upper()
        if resp in ['S', 'N']:
            break
        print('Resposta inválida! Digite apenas S ou N.')
    if resp == 'N':
        break
# Mostrando um resumo geral dos jogadores
print('\n--- TABELA DE JOGADORES ---')
print(f'{"Cod":<4} {"Nome":<15} {"Gols":<20} {"Total":<5}') # cod com 4 espacos e jogado para esquerda, nome com 15 e etc
print('-' * 50)
for idx, jogador in enumerate(jogadores): # para indice(cod), jogador em contagem de jogadores
    print(f'{idx:<4} {jogador["nome"]:<15} {str(jogador["gols"]):<20} {jogador["total"]:<5}')
    # printa o cod    o nome  os gols e o total de gols
print('-' * 50)
# Consulta de dados individuais
while True:
    busca = input('\nMostrar dados de qual jogador? (Digite o código ou "999" para sair): ')
    # buscar jogador por codigo
    if not busca.isdigit():
    # se a busca nao for um digito
        print('Por favor, digite um número válido.')
        continue
    busca = int(busca) # transforma em int, nem precisava disso, mas ok
    if busca == 999:
        print('Finalizando...')
        break
    elif 0 <= busca < len(jogadores):
        jogador = jogadores[busca]
        print(f'-- LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
        for i, g in enumerate(jogador['gols']):
        # para cada jogador, gols em contagem jogador
            print(f'   No jogo {i + 1} fez {g} gol(s)')
    else:
        print(f'Código inválido. Digite um número entre 0 e {len(jogadores) - 1} ou 999 para sair.')
