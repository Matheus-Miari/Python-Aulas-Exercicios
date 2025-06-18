# ler numero inteiro
# e mostrar na tela n primeiros elementos
# de uma sequencia de fibonacci#


n = int(input('Quantos termos você quer mostrar? ')) # quantos termos
t1 = 0   # termo 1 comeca com 0
t2 = 1   # termo 2 comeca com 1
print(f'{t1} → {t2}', end='')
contador = 3
while contador <= n:  # comeca a contagem ate atingir a meta
    t3 = t1 + t2   # termo3  = a t1 + t2
    print(f' → {t3}', end='')  # printa o termo
    t1 = t2     # t1 assume a posicao da frente
    t2 = t3   # assume a posicao do t3
    contador += 1   # contador

print(' → FIM')
print('~' * 30)