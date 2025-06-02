"""
LER 3 NUMEROS E DIZER QUAL E O MAIOR E MENOR
"""

n1 = int(input('Digite o primeiro numero ai chara: '))
n2 = int(input('Segundo numero paizao: '))
n3 = int(input('Terceiro: '))

maior = max(n1, n2, n3)
menor = min(n1,n2,n3)

print(f'O maior numero digitado foi o {maior} e o menor foi o {menor}')