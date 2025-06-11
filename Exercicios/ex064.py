# ler varios numeros inteiros
# o programa so vai parar quando o usuario
# digitar o valor 999, que a condicao
# de parada, no final ,mostre quantos numeros foram digitados
# e a soma entre eles, desconsiderando 999#

soma = 0
cont = 0
num = 0

while num != 999:
    if num == 999:
        break
    else:
        num = int(input('Digite um numero: '))
        soma += num
        cont += 1
print(f'Contador: {cont}\n Soma: {soma - 999}')
