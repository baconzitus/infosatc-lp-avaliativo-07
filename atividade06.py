lista=[lambda x: x**2 ,lambda x: x*3]

numero=int(input("numero: "))
for x in lista:
    print(x(numero))