'''Programa que muestra los números perfectos entre 1 y 1000'''

def divisores(n):
    '''Devuelve una tupla con los divisores de n'''
    resultado=tuple()
    for i in range(1,n+1):
        if n % i == 0:
            resultado += (i,)
    return resultado

def perfecto(n):
    '''Devuelve el propio número si es perfecto'''
    if sum(divisores(n)) == 2*n:
        return n

lista_perfectos = []
for numero in range(1,1001):
    variable = perfecto(numero)
    if variable:
        lista_perfectos.append(variable)

'''Imprimo el resultado'''        
print(lista_perfectos)
