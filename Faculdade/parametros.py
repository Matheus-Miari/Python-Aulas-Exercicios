# parametros
# dados recebidos pelas funcoes

def realce (s1):    #variavel  entre os parenteses
    print('---*---')
    print(s1)   # vai receber um parametro
    print('===*===')

realce('MENU')

# RESULTADO:
# ---*---
# MENU
# ===*===

# definindo a funcao
def sub2(x, y):
    res = x - y
    print(res)

# CHAMA
sub2(3,8)   #  ordem

sub2(10,2)

sub2( y = 3, x = 15)  # se quiser passar fora de ordem tem que explicitar

# parametros opcionais

def soma3(x,y,z):  # sem paremetros opcionais, sao obrigatorios
    res = x + y + z
    print(res)

def soma4(x = 0,y = 0,z = 0): # se nao passar parametro, a varivel assume o 0, ou fica omitido
    res = x + y + z
    print(res)

soma4(1,2,3)  # 6
soma4(1,2)   # 3 // z foi omitido
soma4(1) # 1 // y e z foram omitidos
soma4()  # todos sao omitidos
