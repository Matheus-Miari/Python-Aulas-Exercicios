"""
ler velocidade de um carro
se ele ultrapassr 80km/hr
mostre um mensagem dizendo que ele foi multado
multa vi custar 7 reais por cada KM ACIMA
do limite
"""
from time import sleep

velocidade = int(input('Qual velocidade tu passou ali chapa: '))
if velocidade > 80:
    print('Tu vai ser \033[31mmultado\033[0m para deixar de ser besta')
    sleep(0.2)
    print(f'Vai pagar \033[31m{(velocidade - 80) * 7.00:.2f}\033[0m R$')
else:
    print('\033[32mSai da minha frente\033[0m')