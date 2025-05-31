# cadeia  de caracteres

frase = 'Batatinha frita 1, 2, 3'
# cada espaco tem um indice, comecando com 0
#fatiamento  ------ range
# print(frase[2:10]) # do indice 2 ate 10 porem o 10 e excluido
## frase[9:21:2] # comecar 9, ate 21 pulando de 2 em 2
# frase[:5] comeca do 0 ate o 5
# frase[15:] comeca com o 15 e vai ate o final
# frase[9::3] comeca com 9, vai ate o final pulando de 3 em 3

#analise da string

print(len(frase)) # comprimento da frase == 23
print(frase.count('a')) # conta os a == 4
print(frase.count('a', 0,13)) # conta frase com fatiamento
print(frase.find('t')) #encontrar
print(frase.replace('frita', 'assada')) #trocaria a frita por assada
frase.upper() #ficaria em maisculo
frase.lower() #ficaria em minusculo
frase.capitalize() #somente a primeira letra fica em maisculo
frase.title() #todas as primeiras letras ficam em maisculos
frase.strip() #remove os espacos inuteis no meio e no final
#rstrip() remove os espacos pela direita
#lstrip() remove os espacos da esquerda
print(frase.split()) # ocorre uma divisao entre as palavras, cada palavra vai ter um indice
print('-'.join(frase)) # juncao de palavras