#ler peso e altura
# calcular imc e
# mostrar status
# menor que 18.5 = abaixo
# 18.5 e 25 = peso ideal
# 25 ate 30 = sobrepreso
# 30 ate 40 = obesidade
# acima de 40 = morbido#

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.1f}")

if imc < 18.5:
    print("Status: Abaixo do peso")
elif imc < 25:
    print("Status: Peso ideal")
elif imc < 30:
    print("Status: Sobrepeso")
elif imc < 40:
    print("Status: Obesidade")
else:
    print("Status: Obesidade mórbida")
