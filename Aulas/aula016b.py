a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)  # (2, 5, 4, 5, 8, 1, 2) juntou as tuplas, ordem faz direnca
print(len(c)) # 7
print(c.count(5)) # Contando quantas vezes o item aparece == 2
print(c.index(8)) # em que posicao esta o item == 4

pessoa = ('Matheus',25,'M', 66.88) # Dados diferentes em tuplas
del(pessoa) # deleta
print(pessoa)  # ('Matheus', 25, 'M', 66.88) // NameError: name 'pessoa' is not defined