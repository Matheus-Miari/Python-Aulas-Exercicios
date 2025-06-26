# tupla preenchia de 0 ate 20
# o usuario vai digitar o numero:
# o programa retorna o numero por extenso

numeros = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

num = int(input('Digite um numero: '))

while num < 0 or num > 20:
    num = int(input('Digite um numero valido: '))

print(f'O numero digitado foi {numeros[num]}')