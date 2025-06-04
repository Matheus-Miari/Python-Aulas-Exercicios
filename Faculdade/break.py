# encerrar um laco
""" print('Digite um texto')
print('Para encerrar escrevar "sair"')"""

''' while True :
    texto = input('')
    print(texto)
    if texto == 'sair':
        break  # para o laco
print('Encerrando o programa') '''

# continue

while True:
    nome = input('Qual e seu nome: ')
    if (nome != 'Matt'):
        continue #volta para o inicio
    senha = input('Senha: ')
    if (senha == 'may'):
        break #encerra
    print('Acesso concedido')