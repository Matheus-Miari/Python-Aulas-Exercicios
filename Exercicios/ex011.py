#programa que leia altura e largur em metros
# calculca a area
# quantidde de tint necessaria para pintala
# cada litro = 2m2

altura = float(input('Altura: '))
largura = float(input('Largura: '))
area = altura * largura
tinta = area / 2
print(f'A area total: {area}m\nAcho que vai dar uns {tinta:.2f}l de tinta pae')