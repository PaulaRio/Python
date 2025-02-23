
def divisores(n):
    '''Devuelve una tupla con los divisores de n'''
    resultado=tuple()
    for i in range(1,n+1):
        if n % i == 0:
            resultado += (i,)
    return resultado

lista=[1,2,3,6,7,11]
print(list(filter(lambda x:len(divisores(x))==2 and x,lista)))