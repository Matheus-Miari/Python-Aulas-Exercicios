# ler nome, ano de nascimento, carteira de trabalho
# e cadastrar a IDADE, em um dicionario
# se CTPS for diferente de zero,
# o dicionario tbm recebera o ano de contratacao
# e o salario. calcular quantos anos
# a pessoa vai se aposentar
# saida: nome, ano, ctps, ano de contratacao, salario
# aposentadoria 35 anos de contribuicao #


lista = []

from datetime import date
ano_atual = date.today().year

while True:
    func = {}
    func['nome'] = str(input('Nome: '))
    func['anodenasc'] = int(input('Ano de nascimento: '))
    func['idade'] = ano_atual - func['anodenasc']
    func['ctps'] = int(input('CTPS (0 se nao tem): '))
    if func['ctps'] != 0:
        func['anoContratacao'] = int(input('Ano de contratação: '))
        func['salario'] = float(input('Salário: R$ '))
        func['anoAposenta'] = func['anoContratacao'] + 35
        func['idadeAposenta'] = func['anoAposenta'] - func['anodenasc']
    else:
        func['salario'] = float(input('Salário: R$ '))
        func['anoContratacao'] = ano_atual
        func['anoAposenta'] = func['anoContratacao'] + 35
        func['idadeAposenta'] = func['anoAposenta'] - func['anodenasc']

    lista.append(func.copy())

    resp = str(input('Quer continuar [S/N]? ')).upper()
    if resp == 'N':
        break

print('CADASTRO: ')
for pessoa in lista:
    print('-'*30)
    print(f'Nome: {pessoa['nome']}')
    print(f'Ano nascimento: {pessoa['anodenasc']}')
    print(f'Idade: {pessoa['idade']}')
    print(f'Ctps: {pessoa['ctps']}')
    print(f'Ano de aposentadoria: {pessoa['anoAposenta']}')
    if pessoa['ctps'] != 0:
        print(f"Ano de contratação: {pessoa['anoContratacao']}")
        print(f"Salário: R$ {pessoa['salario']:.2f}")
        print(f"Idade para aposentadoria: {pessoa['idadeAposenta']}")
        print(f'Ano de aposentadoria: {pessoa['anoAposenta']}')
    else:
        print(f"Ano de contratação: {pessoa['anoContratacao']}")
        print(f"Salário: R$ {pessoa['salario']:.2f}")
        print(f"Idade para aposentadoria: {pessoa['idadeAposenta']}")
        print(f'Ano de aposentadoria: {pessoa['anoAposenta']}')