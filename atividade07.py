
def Conceito(media,aluno):
    if media>=0 and media<=4.9:
        print("O aluno",aluno,"tem media:",media,"e um conceito de: D")
    elif media>=5 and media<=6.9:
        print("O aluno",aluno,"tem media:",media,"e um conceito de: C")
    elif media>=7 and media<=8.9:
        print("O aluno",aluno,"tem media:",media,"e um conceito de: B")
    elif media>=9 and media<=10:
        print("O aluno",aluno,"tem media:",media,"e um conceito de: A")
    else:
        print("!!!")

lista_media=[]

for x in range(10):
    lista_media.append(((lambda x,y:x+y)((float(input("nota 1 de 0 a 4: "))),(float(input("nota 2 de 0 a 6: "))))))
for x in range(10):
    Conceito(lista_media[x],x+1)


 
