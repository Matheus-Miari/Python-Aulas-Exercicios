# string = imutavel

s1 = 'Algoritmos'
print(s1)
# s1[0] = 'a'  ## error

s1 = list('Algoritmos')  # lista que contem a string
print(s1)  # ['A', 'l', 'g', 'o', 'r', 'i', 't', 'm', 'o', 's']
print(''.join(s1))  # Algoritmos

s1[0] = 'a'
print(''.join(s1)) # algoritmos agr muda pq e uma lista

