# 1. Determina la longitud de la cadena "Hola mundo".
cadena1 = "Hola mundo"
print(len(cadena1))

# 2. Muestra los últimos cuatro caracteres de la cadena "Programación en Python".
cadena2 = "Programación en Python"
print(cadena2[-4:])

# 3. Imprime por pantalla los caracteres en las posiciones impares de la cadena "abcdefghijkl".
cadena3 = "abcdefghijkl"
print(cadena3[1::2])

# 4. En mayúscula, muestra los caracteres en posiciones múltiplo de cinco de la cadena "".
cadena4 = "Multiplo de cinco en esta cadena"
print("".join([c.upper() for i, c in enumerate(cadena4) if i % 5 == 0]))

# 5. De tres en tres, imprime del carácter en la posición 2 al de la posición 20 de la cadena "Ejercicios de Python".
cadena5 = "Ejercicios de Python"
print(cadena5[2:21:3])

# 6. Verifica si la cadena "información" contiene la subcadena "ma".
cadena6 = "información"
print("ma" in cadena6)

# 7. Determina si la cadena "Python es divertido" comienza con la palabra "Python".
cadena7 = "Python es divertido"
print(cadena7.startswith("Python"))

# 8. ¿Está presente la letra "z" en la cadena "Caza zorros en la zona"?
cadena8 = "Caza zorros en la zona"
print("z" in cadena8)

# 9. ¿La cadena "Examen final" contiene la palabra "final" en mayúscula o minúscula?
cadena9 = "Examen final"
if("final" in cadena9.lower()):
    print("En minuscula")
else:
    print("En mayuscula")

# 10. Divide la cadena "Análisis de datos" en palabras y únelas con guiones bajos.
cadena10 = "Análisis de datos"
print("_".join(cadena10.split()))

# 11. Cuenta las consonantes en la cadena "Inteligencia artificial".
cadena11 = "Inteligencia artificial"
vocales = "aeiouAEIOU"
consonantes = [c for c in cadena11 if c.isalpha() and c not in vocales]
print(len(consonantes))

# 12. Reemplaza las letras "a" por "o" en la cadena "La manzana está en la mesa".
cadena12 = "La manzana está en la mesa"
print(cadena12.replace("a", "o"))