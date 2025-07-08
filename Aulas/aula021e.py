def teste(b):
    global a # nao crie a variavel, use a global/coloque na global
    a = 8
    b += 4 # escopo local
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5 # escopo global
teste(a)
# b e c dao erro pq sao escopos locais
print(f'O a fora vale {a}')