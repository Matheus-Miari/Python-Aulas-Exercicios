# ler ano de nasc de 7 pessoas
# no final, mostrar quantas pessos ainda
# nao atingiram a maioridade e quantas ja sao
# maiores#

from datetime import datetime

ano_atual = datetime.now().year
cont_menor = 0
cont_maior = 0

for c in range(0,7):
    idd = int(input('Digite seu ano de nascimento: '))
    if ano_atual - idd < 18:
        cont_menor = cont_menor + 1
    else:
        cont_maior = cont_maior + 1
print(f'Menores: {cont_menor} \n Maiores: {cont_maior}')
