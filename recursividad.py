def sumatorio(n):
    if n==1:
        return 1
    else:
        return sumatorio(n-1)+n
    
'''Programa principal'''
numero= int (input('Introduce un numero para realizar el sumatorio: '))
print(sumatorio(numero))