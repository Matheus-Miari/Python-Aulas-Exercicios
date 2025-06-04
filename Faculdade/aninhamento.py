# podemos misturar while e for

# tabuadda com while e for

# 2x while

""" tabuada = 1
while tabuada <= 10:
    print(f'Tabulada do {tabuada}')
    i = 1
    while i <= 10:
        print(f'{tabuada} x {i} = {tabuada * i}')
        i += 1
    tabuada+=1  """

# 2x for

for tabuada in range(1,11,1):
    print(f'Tabuada dor {tabuada}')
    for i in range(1,11,1):
        print(f'{tabuada} x {i} = {tabuada * i}')