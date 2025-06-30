galera = [['Matt', 25],['May', 24],['Tenis', 30],['Pedro', 34]]

print(galera) # [['Matt', 25], ['May', 24], ['Tenis', 30], ['Pedro', 34]]
print(galera[0]) # ['Matt', 25]
print(galera[0][0]) # Matt
print(galera[2][1]) # 30
print(galera[3]) # ['Pedro', 34]

for p in galera:
    print(p[0])
    #Matt
    #May
    #Tenis
    #Pedro

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade..')
    #Matt tem 25 anos de idade..
    #May tem 24 anos de idade..
    #Tenis tem 30 anos de idade..
    #Pedro tem 34 anos de idade..