exponentes = list(range(1, 11))  # Lista de los números del 1 al 10

# a) ¿Qué tenemos en la lista? (en lenguaje natural)
# Respuesta en lenguaje natural: "Tenemos los números del 1 al 10."
print("a)", exponentes)

# b) Añadir a la lista de exponentes [18, 19]
exponentes.extend([18, 19])
print("b)", exponentes)

# c) Para cada elemento de la lista, imprimir por pantalla 2 ** x
print("c) Potencias de 2:")
for x in exponentes:
    print(f"2 ** {x} = {2 ** x}")

# d) Para cada elemento de la lista, imprimir por pantalla su cuadrado
print("d) Cuadrados:")
for x in exponentes:
    print(f"{x} ** 2 = {x ** 2}")

# e) Mostrar los resultados del ejercicio anterior en orden inverso
print("e) Cuadrados en orden inverso:")
for x in reversed(exponentes):  # Usamos reversed para iterar de atrás hacia adelante
    print(f"{x} ** 2 = {x ** 2}")

# f) Comprobar si 2 ** x es un número par
print("f) Comprobación de paridad de 2 ** x:")
for x in exponentes:
    if (2 ** x) % 2 == 0:
        print(f"2 ** {x} = {2 ** x} es par")
    else:
        print(f"2 ** {x} = {2 ** x} es impar")

# g) Imprimir cada elemento de la lista junto a su posición (índice)
print("g) Elementos con su índice:")
for idx, x in enumerate(exponentes):
    print(f"Índice {idx}: {x}")

# h) Obtener la suma de calcular 7 ** x para cada elemento de la lista
suma = 0
print("h) Suma de potencias de 7:")
for x in exponentes:
    suma += 7 ** x
print(f"Suma de las potencias de 7: {suma}")

# i) Detenerse cuando el valor acumulado sea mayor que 200
suma = 0
print("i) Suma de potencias de 7 (se detiene cuando la suma es mayor que 200):")
for x in exponentes:
    suma += 7 ** x
    if suma > 200:
        print(f"Se detuvo en x = {x} con una suma acumulada de {suma}")
        break
