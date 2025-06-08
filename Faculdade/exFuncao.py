# escreva uma funcao para validar uma string
# essa funcao recebe como parametros a string,
# o número minimo e maximo de caracteres
# retorne verdadeiro se o tamaanho da string estiver
# entres os valores minimo e maximo
# falso caso contrario #

def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tan = len(s1)
    while ((tan < min)) or (tan > max):
        s1 = input(pergunta)
        tan = len(s1)
    return s1

# chama

x = valida_string('Digite uma frase: ', 10, 30)
print(f'Vc digitou a string: {x}')

