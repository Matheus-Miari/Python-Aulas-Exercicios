# forca o programa a nao criar uma variavel local
# de mesmo nome e manipular somente a global
# dentro de uma funcao

def ometele():
    global ovos   # ai sim o print vai sair 6 == INSTRUCAO GLOBAL
    ovos = 6

ovos = 12
ometele()
print(ovos)   ## 12

