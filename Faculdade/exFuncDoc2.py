#Colecionador de jogos
# escreva um algoritmos que permita cadastrar esse jogos informando o nome
# e qual videogame ele pertence
# crie um  menu de opcoes contendo:
# cadadstrar novo item, listar tudo que foi cadstrado e sair #
# uma funcao para cada item #
#
from os.path import exists

#R = LEITURA
# W = ESCRITA, APAGA O CONTEUDO SE JA EXISTIR
# A = ESCRITA MAS PRESERVA O CONTEUDO
# B = MODO BINARIO
# + = ATUALIZACAO#

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criacao...')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso ! \n')

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideoGame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write(f'{nomeJogo}; {nomeVideoGame} \n')
    finally:
        a.close()
def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        print(a.read())
    finally:
        a.close()

""" PROGRAMA PRINCIPAL"""

arquivo = 'games.txt'

if existeArquivo(arquivo):
    print('Arquivo localizado')
else:
    print('Arquivo inexistente')
    criarArquivo(arquivo)

while True:

    print('Menu')
    print('1 - Cadastrar novo item \n 2 - Listar cadastrado \n 3 - Sair')
    op = valida_int('Escolha a opcao desejada: ', 1, 3)

    if (op == 1): # novo item
        print('Cadastrar novo item')
        nomeJogo = input('Nome do jogo: ')
        nomeVideoGame = input('Nome do video game: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideoGame)

    elif (op == 2): # LISTAR ITEMS
        print('Listando: ')
        listarArquivo(arquivo)

    else: # SAIR
        print('Encerrando...')
        break