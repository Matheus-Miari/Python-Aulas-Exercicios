def teste():
    x = 9
    print(f'Na funcao teste, o x vale {x}')
    print(f'Na funcao teste, n vale {n}')

n = 2 # escopo global

print(f'No principal, n vale {n}')
teste()
# print(f'No principal, x vale {x}') # erro ele quebra pq x so vale no escopo local


