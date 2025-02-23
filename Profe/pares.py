def pares(n):
    '''Función generadora que devuelve números pares hasta el n'''
    for i in range(n+1):
        if i % 2 == 0:
            yield i

'''Principal'''
for numero in pares(10):
    print(numero)
    
'''si quiero tener el control, con la función next'''    

iterador = pares(10)
print(next(iterador))
print(next(iterador))
print(next(iterador))

'''Uso de la función iter()'''

lista = [1,2,3,4,5]
lista_iterable = iter(lista)
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))
