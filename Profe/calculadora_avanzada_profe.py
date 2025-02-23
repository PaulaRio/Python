def operacion(a,b,funcion):
    return funcion(a,b) 

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def producto(a,b):
    return a*b

def division(a,b):
    return a / b

print(operacion(6,7,suma))
print(operacion(6,7,resta))
print(operacion(6,7,producto))
operacion(6,7,print)