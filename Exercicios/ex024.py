# LER UM NOME DE UMA CIDADE
# E DIZER SE COMECA OU NAO COM SANTO
# #

cidade = str(input('Digite o nome da sua cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')