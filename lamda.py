def suma(a,b):
    return a+b

c=lambda a,b:a+b
print(suma(3,4))
print(c(3,4))

'''Funcion para saber si num es par'''
def impar(n):
    return n%2!=0
print(impar(5))
'''Lambda:'''
c=lambda n:n%2!=0
print(c(5))