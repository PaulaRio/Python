'''a)Imprime por pantalla todas las potencias de 2 menores o 
iguales que 2048, utilizando un bucle while.'''
import statistics


i=1
while(2**i<=2048):
    print(2**i)
    i+=1

'''b)Lee valores del usuario hasta que teclee un número par, 
utilizando un bucle while.'''
num=1
while(num%2!=0):
    num=int(input("Introduce un num "))

'''c)Imprime por pantalla las primeras 15 potencias de 2.'''
i=1
while(i<=15):
    print(2**i)
    i+=1

'''d)Lee una cadena de texto del usuario y 
para cada letra indica si es una vocal o una consonante.'''
cad=input("Introduce una cadena ")
vocales="AEIOUaeiou"
for c in cad:
    if(c in vocales):
        print(c,"es una vocal")
    else:
        print(c,"es una consonante")

'''e)A partir de 2 listas de enteros, 'numeros1' y 'numeros2', 
crea una lista que contiene aquellos valores de la primera 
que también están en la segunda e imprímela por pantalla. 
Es decir, calcula la intersección de ambas listas.'''
numeros1 = [1, 7, 13, 21, 27, 29, 34, 48, 50, 51, 53, 61, 68, 74, 82, 83, 84, 87, 92, 94]
numeros2 = [4, 6, 10, 18, 23, 29, 30, 32, 43, 54, 55, 55, 71, 76, 77, 82, 88, 92, 94,95]
interseccion=[]
for num1 in numeros1:
    if(num1 in numeros2):
        interseccion.append(num1)
print(set(interseccion))

'''f)A partir de 2 listas de enteros, 'numeros1' y 'numeros2'
de igual tamaño, generar otra cuyo primer elemento es el producto del
primer elemento de las listas 'numeros1' y 'numeros2',
 y así sucesivamente.'''
numeros1 = [1, 7, 13, 21, 27]
numeros2 = [4, 6, 10, 18, 23]
multi=[]
for num1,num2 in zip(numeros1,numeros2):
    multi.append(num1*num2)
print(multi)

'''g)A partir de 2 listas de enteros, 'numeros1' y 'numeros2',
 almacenar en una lista el resultado de multiplicar cada uno de los 
 elementos de 'numeros1' por, a su vez, cada uno de los elementos 
 de 'numeros2'. Es decir, 
 la lista resultante tendrá len(numeros1) * len(numeros2) elementos.'''
numeros1 = [1, 7, 13, 21, 27] 
numeros2 = [8, 9, 28, 41, 55, 77]
multi=[]
for num1 in numeros1:
    for num2 in numeros2:
        multi.append(num1*num2)
print(len(multi))
'''h)Para cada una de las cadenas de texto almacenadas en una lista,
 imprimir por pantalla el índice y la cadena en sí e indicar si la 
 palabra es demasiado corta (5 o menos caracteres) o larga (más de 5 caracteres)'''
frase = " Programmers are, in their hearts, architects, and the first thing they want to do when they get to a site is to bulldoze the place flat and build something grand "
lista=frase.replace(","," ").split()
print(lista)
for i,word in enumerate(lista):
    if(word!=""):
         print(f"Indice: {i+1}  cadena: {word} es larga: {len(word)>5}") 
'''i)Recibe una lista de enteros y calcula la media aritmética.'''
enteros = [1, 5, 9, 12, 13, 19, 23, 27, 29, 30, 57, 59, 67, 83, 92, 98, 100]
print(sum(enteros)/len(enteros))
print(statistics.mean(enteros))
'''j)Lee una cadena de texto del usuario e imprime por
 pantalla un mensaje si y solo si la cadena es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''
cadena=input("Introduce una cadena ")
lista=list(cadena)
ptmedio=len(cadena)//2
palindromo=True
i=0
while(i<=ptmedio and palindromo):
    if(lista[i]==lista[-(i+1)]):
        i+=1
        palindromo=True
    else:
        palindromo=False
print(f"Es palindromo {palindromo}")

'''cadena = input("Introduce una cadena: ").replace(" ", "").lower()  
lista = list(cadena)  
ptmedio = len(cadena) // 2  
palindromo = True  

for i in range(ptmedio):  
    if lista[i] != lista[-(i + 1)]:  
        palindromo = False
        break 

print(f"Es palíndromo: {palindromo}")
'''
    
