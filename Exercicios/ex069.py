# ler o sexo de varias pessoas, a cada pessoa
# cadastrada, o programa deve perguntar
# se o usuario quer continuar
# mostrar:
# quantas pessoaas tem +18
# quantos homenes
# quantas mulheres tem menos de 20#


n_pessoas = 0
sex_pessoas = 0
qtdMaiores = 0
quantosHomens = 0
mulheresMenosVinte = 0

print('--FICHA DE CADASTRO--')

while True:
    nome_pessoa = str(input('Nome: '))
    sexo_pessoa = str(input('Sexo: ')).strip().upper()
    idade_pessoa = int(input('Idade: '))
    n_pessoas += 1
    if idade_pessoa > 18:
        qtdMaiores += 1
    if sexo_pessoa == 'M':
        quantosHomens += 1
    if sex_pessoas == 'F' and idade_pessoa < 20:
        mulheresMenosVinte += 1
    continuar = str(input('Deseja continuar: ')).strip().upper()
    if continuar != 'S':
        break
print(f'Resultados finais Pessoas +18: {qtdMaiores} \n Homens: {quantosHomens} \n Mulheres menos 20: {mulheresMenosVinte}')