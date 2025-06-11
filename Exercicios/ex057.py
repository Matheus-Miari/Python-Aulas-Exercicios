# faca um programa que leia sexo de uma pessoa
# mas so aceite valores M ou F #

sex = input('Sexo [M/F]: ').upper().strip()
while sex not in ['M', 'F']:
    sex = input('Valor inválido. Sexo [M/F]: ').upper().strip()
print('Sexo registrado com sucesso!')
