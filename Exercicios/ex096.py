# chama uma funcao chamada area()
# receba as dimensoes de um terrno retangular
# largura e comprimento
# e mostre a area do terreno
# SAIDA:
# LARGURA:
# COMPRIMENTO:
# AREA #

def area(largura, comprimento):
    areaTotal = largura * comprimento
    print(f'Largura do terreno: {largura:.2f}m2 \nComprimento: {comprimento:.2f}m2 \nArea total: {areaTotal:.2f} m2')


area(
    largura= float(input('Largura: ')),
    comprimento=float(input('Comprimento: '))
)
