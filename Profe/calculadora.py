#espacio de trabajo p.ej. /usr/bin/python3
#codificacion utf-8

'''Ejemplo de módulo en Python que se puede
utilizar como una calculadora'''

__author__ = 'José Miguel'
__copyright__ = 'Derechos'
__license__ ='MIT'

def suma(a,b):
    print('El resulta de la suma ', a+b)
    return a+b

def resta(a,b):
    print('El resultado de la resta',a-b)
    return a-b

def multiplicacion(a,b):
    print('El resultado de la multiplicación es',a*b)
    return a*b

def division(a,b):
    print('El resultado de la división es', a/b)
    return a/b

if __name__=="__main__":
    print("ejecutando como programa principal")
    suma(10,10)
else:
    print('el módulo está siendo importado')