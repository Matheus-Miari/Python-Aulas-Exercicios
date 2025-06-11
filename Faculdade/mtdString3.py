# capitalize() - Deixa a primeira letra maiúscula
s = "python"
print(s.capitalize())  # Saída: 'Python'

# lower() - Converte toda a string para minúsculas
s = "Python É Legal"
print(s.lower())  # Saída: 'python é legal'

# upper() - Converte toda a string para maiúsculas
s = "Python é legal"
print(s.upper())  # Saída: 'PYTHON É LEGAL'

# strip() - Remove espaços em branco nas extremidades
s = "  Python  "
print(s.strip())  # Saída: 'Python'

# replace() - Substitui parte da string por outra
s = "Eu gosto de Python"
print(s.replace("Python", "programar"))  # Saída: 'Eu gosto de programar'

# split() - Divide a string em uma lista
s = "maçã,banana,laranja"
print(s.split(","))  # Saída: ['maçã', 'banana', 'laranja']

# join() - Junta elementos de uma lista em uma string
frutas = ['maçã', 'banana', 'laranja']
print(", ".join(frutas))  # Saída: 'maçã, banana, laranja'

# find() - Retorna o índice da primeira ocorrência (ou -1 se não encontrar)
s = "Eu gosto de Python"
print(s.find("Python"))  # Saída: 12

# startswith() - Verifica se a string começa com um valor específico
s = "Python é incrível"
print(s.startswith("Python"))  # Saída: True

# endswith() - Verifica se a string termina com um valor específico
s = "arquivo.txt"
print(s.endswith(".txt"))  # Saída: True

# count() - Conta quantas vezes uma substring aparece
s = "banana"
print(s.count("a"))  # Saída: 3

# isdigit() - Verifica se a string contém apenas dígitos
s = "12345"
print(s.isdigit())  # Saída: True

# isalpha() - Verifica se a string contém apenas letras
s = "Python"
print(s.isalpha())  # Saída: True

# title() - Converte a string para formato de título
s = "python é incrível"
print(s.title())  # Saída: 'Python É Incrível'
