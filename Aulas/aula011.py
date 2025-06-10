# CORES EM PYTHON
# codigo ansi

# cores = \033[stlye;text;backgroundm
# exemplo = \033[0;33;44m

# style = 0, 1, 4, 7
# 0 - none
# 1 - bold
# 4 - underline
# 7 - negativo -- inverte

#text =
'''
30 = white
31 = red
32 = green
33 = yellow
34 = blue
35 = purple
36 = ciano
37 = cinza
'''

#background
"""
40 = white
41 = red
42 = green
43 = yellow
44 = blue
45 = purple
46 = ciano
47 = cinza """

print('\033[1;30;41m Teste \033[m')
print('\033[4;33;46m Teste \033[m')
print('\033[0;35;43m Teste \033[m')
print('\033[30;42m Teste \033[m')
print('\033[m Teste \033[m')
print('\033[7;30m Teste \033[m')