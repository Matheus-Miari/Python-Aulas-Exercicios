# ler data de nascimento de um atleta
# e mostre sua categoria
# ate 9 anos = mirim
# ate 14 = infantil
# ate 19 = junior
# ate 22 = senior
# acima - master#

from datetime import datetime

data_nasc = int(input('Ano de nascimento do atleta: '))
ano_atual = datetime.now().year
idade = ano_atual - data_nasc

print(f"Idade: {idade} anos")

if idade <= 9:
    print("Categoria: Mirim")
elif idade <= 14:
    print("Categoria: Infantil")
elif idade <= 19:
    print("Categoria: Júnior")
elif idade <= 22:
    print("Categoria: Sênior")
else:
    print("Categoria: Master")
