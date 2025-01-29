import random


def acertar(n,intento=1):
    entrada=int(input('Adivina el numero entre 1 y 10: '))
    if entrada<n:
        print (f'El numero {entrada} es demasiado pequeño')
        acertar(n,intento+1)
    elif entrada>n:
        print (f'El numero {entrada} es demasiado grande')
        acertar(n,intento+1)
    else: 
         print (f'Has acertado en el intento: {intento}')


    
    
'''Programa principal'''
numero= random.randrange(10)
acertar(numero)