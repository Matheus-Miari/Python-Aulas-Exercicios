# FUNÇÕES PARTE 1 = TEORIA
# ROTINA = FUNÇÃO
# PRINT() - LEN() - INPUT() SÃO FUNÇÕES

def mostraLinha():  # criou um funcao
    print('*-*'*20)

# DUAS LINHAS VAZIAS, QUESTAO DE ESTETICA
mostraLinha() # chamou a funcao
print(f'{"MATHEUS":^60}')
mostraLinha()

def mensagem(msg): # RECEBE UM PARAMETRO
    print('-'*60)
    print(f'{msg:^60}')
    print('-' * 60)


mensagem('PARAMETRO') # CHAMA A FUNCAO E PASSA O PARAMETRO
mensagem('CONTEUDO')
mensagem('PYTHON É LEGAL DEMAIS')