'''Adivina un número del 1 al 10'''
import random

'''Usaremos una función recursiva'''
def adivinar(num, intento=1):
    entrada = int(input('Adivina el número (entre 1 y 10): '))
    if entrada < num:
        print(f'El número {entrada} es demasiado pequeño')
        adivinar(num, intento+1)
    elif entrada > num:
        print(f'El número {entrada} es demasiado grande')
        adivinar(num, intento+1)
    else:
        print(f'Enhorabuena has acertado el número {entrada} en el intento {intento}')

'''Programa principal'''
numero = random.randint(1,10)
adivinar(numero)