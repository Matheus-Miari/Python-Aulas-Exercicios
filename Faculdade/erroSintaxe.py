# COMO CORRIGIR ERROS DE SINTAXE
# ERRO DE DIGITACAO, IDENTACAO, PALAVRA-CHAVE
from orca.debug import printTokens

#EXCECOES COMUNS EM PYTHON - - - - - - - -  - -
# zeroDivisionError - erro de divisao por zero
# ValueError - erro de um dado nao espero sendo digitado
# IndexError - erro de indice inexistente sendo acessado

while True:
    try:  # tente
        x = int(input('Digite um numero: '))
        break  # encerre
    except ValueError:  # se der VALUERROR : PRINT = = = =
        print('Ooops ! Numero invalido. Tente novamente . . .')

### cortornamos o erro de value error

i = 0
while True:
    try:
        nome = input('Digite seu nome: ').strip()
        ind = int(input('Digite o indice do que quer acessar: '))
        print(nome[ind])
        break
    except ValueError:
        print('Oops ! Nome invalido. Tente Novamente  . . .')
    except IndexError:
        print('Oops ! Indice invalido. Tente novamente . . . ')
    finally: ### sempre acontece, faz a contagem de tentativas
        print(f'Tentativa {i}')
        i += 1

