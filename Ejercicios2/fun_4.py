def seek(lista,n):
    if(n in lista):
        return lista.index(n)
    else:
        return -1
    
lista=[1,2,3,45,6]
print(seek(lista,47))
    