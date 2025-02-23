'''Programa que imprime por pantalla
los numeros primos del 1 al 100
'''
def primos_list(n):
    '''Devuelve primos de n'''
    list=[]
    for i in range(1,n+1):
        if i%i==0:
            list.append(i)
    return list

def divisores_tupla(n):
    '''Devuelve una tupla con los divisores de n'''
    resultado=tuple()
    for i in range(1,n+1):
        if n % i == 0:
            resultado += (i,)
    return resultado


print(primos_list(49))
print(divisores_tupla(49))
