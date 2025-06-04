#programa que leia
# 2 notas, calcular media
# mostrar aprovado, reprovado ou em recuperacao#

nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))

media = (nota1 + nota2) / 2

print(f"Média: {media:.1f}")

if media >= 7.0:
    print("Situação: Aprovado")
elif 5.0 <= media < 7.0:
    print("Situação: Recuperação ")
else:
    print("Situação: Reprovado")
