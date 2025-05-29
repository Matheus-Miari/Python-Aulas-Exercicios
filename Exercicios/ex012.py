#programa
#que leia um preco de um produto
# e mostre seu novo preco com 5% de desconto
# #
preco = float(input('Preco: R$'))
desconto = 0.05
novo_preco = preco - (preco * desconto)

print(f'Custava: R${preco:.2f}\nCom desconto ficou: R${novo_preco:.2f}')
print(f'O desconto foi de: R${preco*desconto:.2f}')