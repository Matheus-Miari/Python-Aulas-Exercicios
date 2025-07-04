# LER NOME e media de um aluno
# guardando a situacao do aluno
# no final mostrar o resultado
# saida:
# Nome: str
# Media: float'
# Situacao: reprovado/aprovado#
aluno = {} # inicia o dict do aluno
sala = []  # lista de alunos
aprovados = []
reprovados = []
recuperacao = []
while True:  # incia o laco enquanto verdade
    aluno['nome']=str(input('Nome: '))  # nome
    aluno['media']=float(input('Media: ')) # media
    if aluno['media']>7.0:  # se media maior que 7
        aluno['situacao']='Aprovado'  # situacao = aprovado
        aprovados.append(aluno.copy()['nome'])
    elif aluno['media']< 7.0 and aluno['media'] > 6.0:
        aluno['situacao'] = 'Recuperacao'  # situacao = aprovado
        recuperacao.append(aluno.copy()['nome'])
    else:
        aluno['situacao']='Reprovado'
        reprovados.append(aluno.copy()['nome'])
    sala.append(aluno.copy())  # copia para nao sobreescrever
    resp=input('Quer continuar? [S/N] ').upper().strip()   # se quer continuar
    if resp in 'Nn':
        break
for a in sala:  # para cada aluno na sala
    print(f'Aluno: {a["nome"]} = {a["situacao"]}')  # printa  o nome e a situacao dele
print(f'\033[32mAprovados:\033[0m {aprovados}')
print(f'\033[31mReprovados:\033[0m {reprovados}')
print(f'\033[34mRecuperacao:\033[0m {recuperacao} ')