'''La función filter() filtra un iterable eliminando
los elementos que no cumplen con la condición'''

def esnegativo(numero):
    return numero<0

lista = [-9, 0, 3, -4, -1, 8, -13]

a = filter(esnegativo, lista)

print(list(a))

'''La función map() recibe una función y un iterable como argumentos
y devuelve un nuevo iterable con la función aplicada a cada elemento'''

def cuadrado(n):
    return n**2

lista = [-2, 4, 5, 9]

b = map(cuadrado, lista)
print(list(b))