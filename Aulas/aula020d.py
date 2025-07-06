
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7,2,5,3,4]
print(f'Antes da dobra: {valores}' )
dobra(valores)
print(f'Dps da dobra: {valores}')
print(f'Sorted: {sorted(valores)}')