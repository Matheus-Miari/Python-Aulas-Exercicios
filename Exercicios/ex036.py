# programa para aprovar emprestimo bancario para comprar uma
# casa
# perguntar o valor da casa
# o salario do comprador
# quantos anos ele vai pagar
#
# calcular a prestacao mensal, nao pode exceder 30% do salario
# ou entao o emprestimo sera negado#
from time import sleep

print('\033[34m-*-\033[m'*10)
sleep(0.3)
print("--Bem-Vindo ao \033[34mBanco MM\033[m--")

valor_casa = float(input('Qual o valor da casa que voce quer: '))
salario_cliente = float(input('Qual seu salario: '))
anos_pagamento = int(input('Em quantos anos voce pretende pagar: '))
meses_pagando = anos_pagamento * 12
prestacao = valor_casa / meses_pagando
porcentagem_do_salario = salario_cliente * 30 / 100

if prestacao >= porcentagem_do_salario:
    print(f'Vc quer uma casa com um valor de R$ {valor_casa:.3f}\n Quer pagar em {anos_pagamento} anos'
          f'\n Isso da um total de {meses_pagando} meses pagando \n Seu salario de: R$ {salario_cliente:.2f} nao permite a aquisicao'
          f' deste imovel, \n pois 30% do seu salario, corresponde a {porcentagem_do_salario:.2f} e a parcela ficaria em \n'
          f'R$ {prestacao:.2f} logo, nao podemos nos comprometer. Obrigado')
else:
    print(f'Casa: R${valor_casa:.2f}\nAnos: {anos_pagamento}\n Meses: {meses_pagando} \n Salario:R$ {salario_cliente:.2f} \n 30%: R${porcentagem_do_salario:.2f} \n Prestacao:R$ {prestacao:.2f} \n Logo = APROVADO')
