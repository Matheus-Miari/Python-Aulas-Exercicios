# entrada de dados

# leia == input()

# int //   x = int(input("DIGITE: "))
# float //   x = float(input("DIGITE: "))


salario: float
salario2 : float
nome : str
nome2 : str
idade : int
sexo : str

nome = input("Nome: ")
salario = float(input("Salario: "))

nome2 = input("Nome: ")
salario2 = float(input("Salario: "))

idade = int(input('Idade: '))
sexo = input('Sexo: ')

print(f'Nome: {nome}')
print(f'Salario: {salario:.2f}')

print(f'Nome 2: {nome2}')
print(f'Salario: {salario2:.2f}')

print(f'Idade: {idade}')
print(f'Sexo: {sexo}')