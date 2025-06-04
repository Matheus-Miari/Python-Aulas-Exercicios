# calcular media de notas em determinada disciplina
# em 5 notas digitadas

soma = 0
cont = 1
while (cont <= 5):
    nota = float(input(f'Digite a {cont} nota: '))
    soma = soma + nota
    cont = cont + 1
media = soma / 5
print(f'Sua media final foi de {media}')