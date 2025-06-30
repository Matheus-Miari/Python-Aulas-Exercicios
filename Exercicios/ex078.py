# ler 5 valores e guardar em uma lista
# mostrar o maior e o menor e a posicao de cada

lista = [
    int(input('Digite um num: ')),
int(input('Digite um num: ')),
int(input('Digite um num: ')),
int(input('Digite um num: ')),
int(input('Digite um num: '))
]
print(f'A lista indexada: {lista}')
print(f'Maior: {max(lista)}, Pos: {lista.index(max(lista))}')
print(f'Menor: {min(lista)}, Pos: {lista.index(min(lista))}')