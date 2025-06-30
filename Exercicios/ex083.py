# digitar uma expressao que use
# parenteses, seu app devera analisar
# se a expressao passada esta com parenteses abertos e fechdos
# na ordem correta

exp = str(input('Digite a expressao: '))

pilha = []

for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Valida')
else:
    print('Invalida')