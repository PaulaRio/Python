def sumalista(lista):
    try:
        return sum(lista)
    except TypeError:  # Si el elemento no se encuentra en la lista, lanza ValueError
        return "None"   
    
lista=[1,2,3,6,"hola"]
print(sumalista(lista))