# ler 5 valores numericos, jogar em uma lsita
# colocar na posicao ja em ordem sem usar o sort
# no final mostrar ordenada

lista = []
for i in range(5):
    num = int(input(f'Digite o {i+1}º número: '))
    # Se a lista estiver vazia, só adiciona o número
    if len(lista) == 0:
        lista.append(num)
    else:
        inserido = False
        # Percorre a lista para encontrar a posição correta
        for pos in range(len(lista)):
            if num < lista[pos]:
                lista.insert(pos, num)  # Insere na posição correta
                inserido = True
                break
        # Se não foi inserido, é o maior número e vai pro final
        if not inserido:
            lista.append(num)
print(f'Lista ordenada: {lista}')
