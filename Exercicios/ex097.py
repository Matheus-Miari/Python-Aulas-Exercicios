# FUNCAO  ESCREVA()
# RECEBE O TEXTO COMO PARAMETROS
# E MOSTRE  MENSAGEM COM TAMANHO ADAPTAVEL
#

def escreva(texto):
    tam = len(texto) + 4
    print('~'* tam)
    print(f'  {texto}')
    print('~' * tam)

escreva(texto=str(input('Digita um texto ai: ')))