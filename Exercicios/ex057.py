# faca um programa que leia sexo de uma pessoa
# mas so aceite valores M ou F #

sex = input('Sexo [M/F]: ').upper().strip()[0]
while sex not in ['M', 'F']:
    sex = input('Valor inválido. Sexo [M/F]: ').upper().strip()[0]
print(f'Sexo {sex} registrado com sucesso!')