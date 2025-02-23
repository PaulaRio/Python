lista1=[1,2,3,6]
lista2=[2,2,2,2]
resultado =(lambda lista1,lista2: lista1+lista2)(lista1,lista2)#Sin map hace falta pasar parametros
print(list(resultado))

'''concatenar = lambda s1, s2: s1 + s2

print(concatenar("Hola ", "mundo!"))'''