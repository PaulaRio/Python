'''
Crea una función convencional que calcule la media de una
lista de números y usa map() para hallar la media de cada
lista.
Luego reescribe el código reemplazando la función por una
expresión lambda dentro de la llamada a map()'''
def media(list):
    return sum(list)/len(list)


numeros= [[57, 12, 94, 44, 19],[58, 84, 15, 76,44],[48, 58, 92, 81, 63],[44, 57, 19, 94, 12]]
'''Utilizando una funcion convencional'''
print(list(map(media,numeros)))
'''Utilizando lambda'''
print(list(map(lambda lista_num: sum(lista_num)/len(lista_num),numeros)))



