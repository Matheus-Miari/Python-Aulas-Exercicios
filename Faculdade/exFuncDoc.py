# Uma funcao que calcula o fatorial de um numero recebido
# como parametro e retorne o seu resultado
# faca uma validacao dos dados por meio de uma outra funcao, perimtindo que somente
# valores positivos sejam aceitos
# CRIE o help da funcao#

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fatorial(num):
    """
    Explicacao da funcao fatorial
    Inicia com fat = 1
    Testa de num == 0, se for entao 0! == fat == 1
    se nao;
    inicia o laco de repeticao for i
    indo de 1 ate numero recebido + 1 para pegar ate o numero escolhido
    indo de 1 em 1
    fat == multiplicado por i == indice
    no final retorna o valor total do fatorial
    :param num:
    :return:
    """
    fat = 1
    if num == 0:  # retorna se num for 0
        return fat
    for i in range(1, num + 1, 1):
        fat *= i
    return fat

x = valida_int('Digite um valor: ', 0, 99999)
print(f'{x}! = {fatorial(x)}')