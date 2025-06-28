num = [2,4,5,6,10]
print(num) # [2, 4, 5, 6, 10]
num[2] = 110
print(num) # [2, 4, 110, 6, 10] LISTA SAO mutaveis
num.append(8) # add o valor 8 a lista
print(num) # [2, 4, 110, 6, 10, 8]
num.sort()
print(num) # [2, 4, 6, 8, 10, 110] em ordem
num.sort(reverse=True)
print(num) #  [110, 10, 8, 6, 4, 2] em ordem descrecente
print(len(num)) # contagem = 6 elementos
num.insert(0, 9) # substitui o 0 pelo 9
print(num) # [9, 110, 10, 8, 6, 4, 2]
num.pop() # removeu o ultimo elemento
print(num) # [9, 110, 10, 8, 6, 4]
num.pop(2) # remove o elemento do indice 2
print(num)  # [9, 110, 8, 6, 4] o 10 foi removido
num.remove(4) # remove o valor passado
print(num) # [9, 110, 8, 6]


