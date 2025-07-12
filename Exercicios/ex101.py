# criar uma funcao que chama voto
# recebe o ano de nascimento
# retorna o valor literal
# indicado se uma pessoa tem voto
# negado, opcional ou obrigatorio
# saida
# ano : (calcular idade)
# saida do voto #

from datetime import datetime

# funcoes
def voto():
    ano_atual = datetime.now().year
    ano_nasc = int(input('Ano de nascimento: '))
    idade = ano_atual - ano_nasc
    print(f'Vc tem {idade} anos. ')
    if idade < 16:
        print(f'Vc ainda \033[31mnao\033[0m pode votar. ')
    if idade < 18 and idade >= 16 or idade > 60:
        print(f'Vc tem \033[34mvoto opcional\033[0m.')
    if idade > 18 and idade < 60:
        print(f'Vc tem voto \033[32mOBRIGATORIO\033[0m.')



# CODIGO PRINCIPAL
titulo = 'Vc pode votar?'
print('='*60)
print(f'{titulo:^60}')
print('='*60)
voto()