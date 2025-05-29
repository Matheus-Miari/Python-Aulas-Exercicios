#escreva um programa que leia um valor em metros
# e converta em cm e mm#
metro = float(input('Digite um valor em metros: '))
cm = metro * 100
mm = metro * 1000
print(f'O valor digitado foi: {metro}\nCentimetro: {cm:.0f}cm\nMilimetros: {mm:.0f}mm')