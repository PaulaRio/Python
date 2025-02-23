def calculadora_avanzada(a,b,operacion):
    if(operacion=="suma"):
         return a+b
    elif(operacion=="resta"):
         return a-b
    elif(operacion=="multiplicacion"):
         return a*b
    elif(operacion=="division"):
         return a/b
    elif(operacion=="potencia"):
         if(b==0):
            print('No se puede dividir entre 0')
            return
         else:
            print(f'El resultado de la division', a/b)
         return a**b
    else:
        print("No has introducido una operacion valida")

print(calculadora_avanzada(5,6,"suma"))


