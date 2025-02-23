# Definimos la lista de números pares del 2 al 100
numeros = list(range(2, 101, 2))

# a) ¿Qué tenemos en la lista?
# Respuesta en lenguaje natural: "Tenemos todos los números pares desde el 2 hasta el 100."
print("a)", numeros)

# b) Los últimos diez elementos de la lista
ultimos_diez = numeros[-10:]
print("b)", ultimos_diez)

# c) Todos los elementos excepto los tres primeros
sin_tres_primeros = numeros[3:]
print("c)", sin_tres_primeros)

# d) Añadimos los valores [13, 12, 11, ..., 2, 1] al final de la lista
extra = list(range(13, 0, -1))
numeros.extend(extra)
print("d)", numeros)

# e) El mínimo de los primeros quince elementos
min_15 = min(numeros[:15])
print("e)", min_15)

# f) Insertamos el mínimo de la lista al final
numeros.append(min(numeros))
print("f)", numeros)

# g) Invertimos el orden de la lista
numeros.reverse()
print("g)", numeros)

# h) La suma de los elementos que tienen índices pares
suma_indices_pares = sum(numeros[i] for i in range(0, len(numeros), 2))
print("h)", suma_indices_pares)

# i) La media aritmética de los elementos de la lista
media = sum(numeros) / len(numeros)
print("i)", media)

# j) A partir de [1, 2, 3, 4, 5], generar [1, 2, 3, 4, 5, 4, 3, 2, 1]
base = [1, 2, 3, 4, 5]
palindromo = base + base[-2::-1]  # Se toma base y se le añade la versión invertida excepto el último elemento
print("j)", palindromo)
