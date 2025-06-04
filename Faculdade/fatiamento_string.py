# FATIAMENTO DE STRINGS
from hpmudext import HPMUD_R_INVALID_DEVICE_NODE

s1 = 'batatinha frita 1,2,3'

print(s1[0:8])  # batatinh

print(s1[8:12]) # a fr

print(s1[:]) # batatinha frita 1,2,3 = pegou tudo

# tamanho da string

tamanho = len(s1)

print(tamanho) # 21

