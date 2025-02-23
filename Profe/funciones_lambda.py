def suma(a,b):
    return a+b


c = lambda a,b: a+b

print(suma(3,4))

print(c(3,4))

'''Función para saber si un número es impar'''

'''Con una función convencional sería:'''
def impar(n):
    return n % 2 != 0

print(impar(5))

'''Con una función lambda:'''        
impar_lambda = lambda numero: numero % 2 != 0

print(impar_lambda(5))









