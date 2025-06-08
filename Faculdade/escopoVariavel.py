# escopo de uma variavel e a propriedade que determina onde uma variavel
# pode ser utilizada dentro de um programa
# ----------------------------------------------------------------------
# escopo local = variaveis criadaas dentro de uma funcao
# escopo global = variaveis dentro do programa principal

def omelete():
    ovos = 12   # variavel local

# omelete()
# print(ovos)  # NameError: name 'ovos' is not defined == erro pois o escopo da varivel - local
# so existe dentro da funcao omelete

def omelete2():
    print(ovos) # escopo local
ovos = 12 # variavel global
omelete2()  # 12

def omelete3():
    ovos = 12
    bacon()
    print(ovos)
def bacon()
    ovos = 6
omelete3()   # ovos igual a 12 pq no BACON a variavel ovos so existe nela


