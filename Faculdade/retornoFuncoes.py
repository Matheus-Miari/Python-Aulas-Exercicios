#funcao x procedimento
# procedure//procedimento = uma rotina sem retorno
# funcao = uma rotina que retorna um dado a quem a invocou #

def soma(x = 0, y = 0, z = 0):
    res = x + y + z
    return res

retornado = soma(1,2,3)   # variavel retornado recebe o RETURN da funcao chamada
print(retornado)   # 6   // print da variavel

print(soma(2,2))   # # 4

