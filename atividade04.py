numeros=[]
for x in range(10):
    print("insira o numero",x+1,":")
    numeros.append(int(input(">")))

impares= filter(lambda x: x%2 ,numeros)
print("impares: ",list(impares))

pares= filter(lambda x: x%2==0 ,numeros)
print("pares: ",list(pares))
