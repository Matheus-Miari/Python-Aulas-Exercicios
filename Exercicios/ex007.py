#desenvolva um programa que leia as duas notas
# de um aluco, calcule e mostre sua media
# bonus= aprovado / reprovado#
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Vc foi \033[32maprovado\033[0m, com uma media de: \033[32m{media}\033[0m')
else:
    print(f'Vc foi \033[31mreprovado\033[0m, sua media foi de: \033[31m{media}\033[0m')
