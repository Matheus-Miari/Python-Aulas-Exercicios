lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original   # isso nao alocada em outro espaco de memoria
# apenas recebeu um apontador para os dados originais

print(lista_original)
print(lista_referenciada)  # [5, 7, 9, 11]  --- [5, 7, 9, 11]

lista_referenciada[0] = 2  #alterou ambos
print(lista_original)
print(lista_referenciada)   # [2, 7, 9, 11]  --- [2, 7, 9, 11]

## COPIA

listaOriginal = [5,7,9,11]
listaReferencia = listaOriginal[:]  # criou um copia
print(listaOriginal)
print(listaReferencia)  # [5, 7, 9, 11] para as duas

listaReferencia[0] = 2 # alterou apenas na referencia
print(listaOriginal)  # [5, 7, 9, 11]
print(listaReferencia)  # [2, 7, 9, 11]