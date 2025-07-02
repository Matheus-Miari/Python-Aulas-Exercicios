# ler nome e duas notas
# no final
# mostrar o boletim com
# a media
# e mostrar notas de cada aluno individualmente
# #

sala = []
mediaAluno = 0

while True:
    aluno = []
    nome = str(input(f'Nome: '))
    primeiraNota = float(input('Primeira nota: '))
    segundaNota = float(input('Segunda nota: '))
    aluno.append(nome)
    aluno.append(primeiraNota)
    aluno.append(segundaNota)
    sala.append(aluno)
    resp = str(input('Deseja continuar? [S/N]: ')).upper()
    if resp in 'N':
        break

print('\nBOLETIM:')
print(f'{"Nº":<4} {"Nome":<10} {"Média":>6}')
print('-' * 25)

for i, aluno in enumerate(sala):
    mediaAluno = (aluno[1] + aluno[2]) / 2
    print(f'{i:<4} {aluno[0]:<10} {mediaAluno:>6.2f}')

while True:
    escolha = input('Notas de qual aluno: ')
    if escolha == '999':
        break
    if escolha.isdigit():
        indice = int(escolha)
        if 0 <= indice < len(sala):
            print(f'Notas de {sala[indice][0]}: {sala[indice][1]}, {sala[indice][2]}')
        else:
            print('Entrada inválida.')