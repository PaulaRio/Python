num= [2, 4, 5]
for i ,numo in  enumerate(num):
    print (i, "->", numo)
print (list(enumerate(num)))

lista1 =[1,3,2,1,4]
lista2=lista1[:]
lista1[1] =10
print(lista2)
print(lista2.pop())
print(lista2)
print(sorted(lista2))
print(sorted(lista2,reverse=True))
print(lista2.index(1))
print(lista2.index(1,2))
lista2.append(1)
print(lista2)
dicccionario = {'one': 1, 'two': 2, 'three':3}
dicccionario["one"]+=1
print(dicccionario)#si se hace una copia con copy el orden de los valores puede ser diferente
print(dicccionario.get("one"))
