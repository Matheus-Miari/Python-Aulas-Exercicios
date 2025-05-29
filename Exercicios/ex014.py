# Escreva um programa que converta uma temperatura
# digitando em
# graus Celsius e converta para graus Fahrenheit.

temp = float(input('Temperatura em Celsius: '))
fare = ((temp*9)/5) + 32
print(f'Convertendo a temperatura: {temp:.2f}°C corresponde a {fare:.2f}°F')