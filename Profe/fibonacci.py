def fibonacci(n):
    '''Generador de n primeros números de Fibonacci'''
    a, b, contador = 0, 1, 0 #inicializamos las variables a y b con los dos primeros elementos
    #el contador nos sirve para controlar hasta cuando hay que generar los números
    while True: #bucle infinito
        if contador > n:
            return #salgo de la función (y del bucle infinito)
        yield a #devuelvo el siguiente elemento
        a, b = b, a+b #se reasignan los valores de a y b
        contador += 1 #incrementamos el contador


'''Principal: genero los primeros 15 números, por ejemplo'''
f = fibonacci(15)
for i in f:
    print(i)
