def pares(n):
    '''Funcion generadora que devuelve numeros pares hasya n'''
    for i in range(n+1):
        if i%2==0:
            yield i
   
'''Principal'''
for numero in pares(10):
    print(numero)
    '''pares =pares(3)'''