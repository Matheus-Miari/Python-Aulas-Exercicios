## doc strings = criar a descricao da funcao

def soma(x = 0, y = 0, z = 0):
    """
    Retorna o somatorio de ate 3 valores numericos quaisquer.
    Todos os parametros sao opcinais.
    x - valor numerico opcional
    y - valor numerico opcional
    z - valor numerico opcional
    """
    return x + y + z
print(soma(3,2,1))
help(soma)