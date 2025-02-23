def divisores(n):
    '''Devuelve una tupla con los divisores de n'''
    resultado=tuple()
    for i in range(1,n+1):
        if n % i == 0:
            resultado += (i,)
    return resultado
def primos(n):
    '''Devuelve una tupla con los primos hasta el n'''
    primos = tuple()
    for numero in range(1,n+1):
        if len(divisores(numero)) == 2:
            primos += (numero,)
    return primos

print(primos(100))
