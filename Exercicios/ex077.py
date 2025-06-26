# tupla com varias palavras
# quais sao as vogais de cada palavra

palavras = (
    "girassol", "montanha", "cachorro", "oceano",
            "vento", "livro", "chave", "janela", "viagem", "neve"
            )

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')