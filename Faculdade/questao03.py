print("Boas-vindas a fabrica de camisetas")
print('Desenvolvido por Matheus Miari')

def escolha_modelo():  # definindo funcao escolha o modelo
    while True:
        print('''Escolha o modelo desejado: 
        Camiseta Manga Curta Simples (MCS) 
        Camiseta Manga Longa Simples (MLS)
        Camiseta Manga Curta Com Estampa (MCE)
        Camiseta Manga Longa Com Estampa (MLE)
        ''')
        modelo = input('Digite o codigo do modelo: ').strip().upper()  # escolhendo, ja colocando em maisculo e tirando os espacos
        if modelo in ['MCS','MLS','MCE','MLE']:  # testa se modelo esta nas opcoes
            return modelo  # retorna o modelo
        else: # se nao, solicita novamente
            print('Opcao invalida. Tente Novamente')

def num_camiseta():  # definindo funcao de qtd de camisa + descontoss
    while True: # inicid o laco enquanto
        try:  # tenta as opcoes
            quantidade= int(input('Digite a quantidade de camisetas: '))
            if quantidade > 20000:  # ja para o codigo se maior que 20 000
                print('Quantidade acima do permitido. Maximo de 20000.')
            elif quantidade <= 0: # opcao invalida se menor que 0
                print('Digite uma quantidade valida.')
            else:  # vai verificar a qtd solicitada e definir o desconto
                if quantidade < 20:
                    desconto = 0
                elif quantidade < 200:
                    desconto = 0.05
                elif quantidade < 2000:
                    desconto = 0.07
                else:
                    desconto = 0.12
                return quantidade, desconto # retorna a quantidade e o desconto
        except ValueError:  # se valor invalido como STR
            print('Valor Invalido. Digite um numero inteiro: ')
print()
def frete():  # define a funcao frete
    while True:
        print('''Escolha o tipo de entrega:
           0 - Retirar na fábrica (R$ 0)
           1 - Transportadora (R$ 100)
           2 - Sedex (R$ 200)''')
        tipo = input("Digite a opção (0/1/2): ").strip()
        if tipo == '0':  # testando as opcoes , vai retornar apenas o escolhido
            return 0
        elif tipo == '1':
            return 100
        elif tipo == '2':
            return 200
        else:
            print('Opcao invalida. Tente novamente')


# CODIGO MAIN

modelo = escolha_modelo()  # chama a funcao de escolher o modelo
qtd_camisetas, perc_desc = num_camiseta()  # chama a funcao de qtd de camiseta e desconto
frete_valor = frete() # chama a funcao frete

precos = {'MCS': 1.80, 'MLS': 2.10, 'MCE': 2.90, 'MLE': 3.20}  # precos das camisetas
valor_unitario = precos[modelo] # pega o preco de acordo com o modelo escolhido e define o valor unitario

valor_total_bruto = valor_unitario * qtd_camisetas  # calcula o valor bruto
valor_desconto = valor_total_bruto * perc_desc # valor do desconto
valor_total = valor_total_bruto - valor_desconto  # valor total com desconto sem frete
valor_total_comFrete =  valor_total_bruto - valor_desconto + frete_valor # com frete

print("\n--- TOTAL ---")
print(f"Modelo escolhido: {modelo}")
print(f"Valor unitário: R$ {valor_unitario:.2f}")
print(f"Quantidade: {qtd_camisetas}")
print(f"Valor sem desconto: R$ {valor_total_bruto}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Total a pagar com Desconto: R$ {valor_total:.2f}")
print(f"Frete: R$ {frete_valor:.2f}")
print(f"Total: R${valor_total_comFrete:.2f}")
