"""
PERGUNTA A DISTANCIA DA VIAGEM EM KM
CALCULE O PRECO DA PASSAGEM, COBRANDO:
0.50 POR KM PARA VIAGENS ATE 200KM
0.45 PARA VIAGENS MAIS LONGAS
"""
dist = float(input('Qual a distancia da sua viajem em KM: '))
if dist <= 200:
    print(f'Vc vai pagar R${dist * 0.50:.2f}')
else:
    print(f'Vc vai pagar R${dist * 0.45:.2f}')