#ler nascimento, e informar
# de acordo com a idade se esta aapto
# para o alistamento militar
# se e hora
#  ou se ja passou
#  mostrar quanto tempo falta#

from datetime import datetime

nasc = int(input('Nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - nasc

if idade < 18:
    print(f'Ainda nao chegou sua hora pai falta {18 - idade} anos, tu tem {idade} anos, vai ser em {ano_atual + (18 - idade)}')
elif idade == 18:
    print(f'O momento e agora, tu tem {idade} anos')
elif idade > 18:
    print(f'Ja passou, foi no ano de {ano_atual - (idade - 18)}, tu tem {idade} anos')