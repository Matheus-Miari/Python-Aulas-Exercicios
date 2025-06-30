# lista p2

teste = list()
teste.append('Math')
teste.append(25)
print(teste) # ['Math', 25]

galera = list()
galera.append(teste)
print(galera) # [['Math', 25]]

galera.append(teste[:])
teste[0] = 'May'
teste[1] = 22
galera.append(teste)
print(galera) # [['May', 22], ['May', 22]]

