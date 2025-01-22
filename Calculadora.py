def suma(a,b):
    print(f'El resultado de la suma', a+b)
    return a+b
def resta(a,b):
    print(f'El resultado de la resta', a-b)
    return a-b
def multiplicacion(a,b):
    print(f'El resultado de la multiplicacion', a*b)
    return a*b
def division(a,b):
    if(b==0):
        print('No se puede dividir entre 0')
        return
    else:
        print(f'El resultado de la division', a/b)
    return a/b
if __name__=="__main__":
    print('Ejecutando como programa principal')
    division(10,0)