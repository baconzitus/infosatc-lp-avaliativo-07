'''
funcao = lambda y: return y
h = funcao(4)
print(h)


o problema e que como a função lambda automaticamente da return em tudo que é True. Ou seja, ela não aceita "return", ela dá automático.
Para consertar erra só retirar o "return" já que como não existe nada para dar False, o número sempre vai ser Troe
tanto que se você colocar y>5 a argumento que volta é um False
Outra coisa quando o argumento volta como booleana o número é perdido mas se houver a necessidade de utilizar esse número e só usar um 
int () que o false volta como 0
'''
funcao = lambda y: y
h = funcao(4)
print(h)

funcao = lambda y: y>5
h = funcao(4)
print(h)

funcao =lambda y:int(y>5)
h = funcao(4)
print(h)