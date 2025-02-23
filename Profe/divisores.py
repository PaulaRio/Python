'''Programa que imprime por pantalla
los divisores de cada número del 1 al 47
'''


def divisores(n):
    '''Devuelve una tupla con los divisores de n'''
    resultado=tuple()
    for i in range(1,n+1):
        if n % i == 0:
            resultado += (i,)
    return resultado

for num in range(1,48):
    print(num, " : ", divisores(num))

