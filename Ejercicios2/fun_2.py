def es_palindromo(cadena):
   cad = cadena.replace(" ", "").lower()  
   lista = list(cad)  
   ptmedio = len(cad) // 2  
   palindromo = True  
   for i in range(ptmedio):  
       if lista[i] != lista[-(i + 1)]:  
           palindromo = False
           break 
    
   if(palindromo):
       return "Es palíndromo "
   else:
       return "No es palíndromo "

print(es_palindromo("Anita lava la tina"))
print(es_palindromo("holi"))

'''def es_palindromo(cadena):

    cadena = cadena.replace(" ", "").lower()

    cont1 = 0
    cont2 = len(cadena) - 1

    while cont1 < cont2:
        if cadena[cont1] != cadena[cont2]:
            return False
        cont1 += 1
        cont2 -= 1

    return True 
    print("palíndromo:", es_palindromo("Anita lava la tina"))
print("palíndromo:", es_palindromo("Hola mundo"))'''