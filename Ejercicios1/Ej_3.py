lista = ["primero", 2, "3.5", 4.0, "ultimo"]

# a) ¿El tamaño de la lista?
tamano_lista = len(lista)
print("a) El tamaño de la lista:", tamano_lista)

# b) El tamaño de la lista multiplicado por su segundo elemento
producto = tamano_lista * lista[1]
print("b) El tamaño de la lista multiplicado por su segundo elemento:", producto)

# c) El producto del segundo elemento de la lista por el tercero
producto_2_3 = lista[1] * float(lista[2])  # Convertimos "3.5" a float para realizar la multiplicación
print("c) El producto del segundo elemento de la lista por el tercero:", producto_2_3)

# d) ¿Está 2 en la lista? ¿Y 2.0?
esta_2 = 2 in lista
esta_2_0 = 2.0 in lista
print("d) ¿Está 2 en la lista?", esta_2)
print("d) ¿Está 2.0 en la lista?", esta_2_0)

# e) Eliminar el primer elemento de la lista
lista.pop(0)
print("e) Lista después de eliminar el primer elemento:", lista)

# f) Eliminar ahora los dos últimos elementos simultáneamente
lista = lista[:-2]  # Eliminamos los dos últimos elementos usando rebanado
print("f) Lista después de eliminar los dos últimos elementos:", lista)

# g) ¿Está la lista vacía?
esta_vacia = len(lista) == 0
print("g) ¿Está la lista vacía?", esta_vacia)

# h) Añadir el elemento "nuevo ultimo" a la lista
lista.append("nuevo ultimo")
print("h) Lista después de añadir el elemento 'nuevo ultimo':", lista)
