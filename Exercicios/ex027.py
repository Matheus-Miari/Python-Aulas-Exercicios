# ler nome completo
# e mostrar primeiro nome
# e ultimo nome separadamente

nome = str(input('Digite seu nome completo: ')).strip()
primeiro = nome.split()
ultimo = primeiro[len(primeiro) - 1]
print(f'Primeiropedr nome: {primeiro[0]}\nUltimo nome: {ultimo}')