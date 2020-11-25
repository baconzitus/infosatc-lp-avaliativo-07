numeros=[]
for x in range(5):
    print("insira o numero",x+1,":")
    numeros.append(int(input(">")))
maiores= filter(lambda x: x>10 ,numeros)
print(list(maiores))

#ou 
'''
numeros=[]
for x in range(5):
    print("insira o numero",x,": ")
    numeros.append(int(input(">")))
maiores= list(filter(lambda x: x>10 ,numeros))
print(maiores)
'''

