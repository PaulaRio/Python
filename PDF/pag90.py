# Inicializa una lista con diferentes tipos de elementos
mi_lista = ["Hola", 3, 4.5, True, [1, 2, 3]]

# 1. ¿Cuál es el tamaño de la lista mi_lista?
print(len(mi_lista))

# 2. Recorre la lista mi_lista e imprime cada elemento.
for elemento in mi_lista:
    print(elemento)

# 3. Calcula el tamaño de la lista multiplicado por el segundo elemento de la lista mi_lista.
resultado_3 = len(mi_lista) * mi_lista[1]
print(resultado_3)

# 4. Calcula el producto del segundo elemento de la lista mi_lista por el tercer elemento.
resultado_4 = mi_lista[1] * mi_lista[2]
print(resultado_4)

# 5. ¿Está el número 5 en la lista mi_lista? ¿Y el número 5.0?
print(5 in mi_lista)
print(5.0 in mi_lista)

# 6. Elimina el primer elemento de la lista mi_lista.
del mi_lista[0]
print(mi_lista)

# 7. Elimina ahora los dos últimos elementos de la lista mi_lista simultáneamente.
del mi_lista[-2:]
print(mi_lista)

# 8. ¿Está la lista mi_lista vacía?
print(len(mi_lista) == 0)
