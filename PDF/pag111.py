# Inicializa una lista con diferentes tipos de elementos
x = [7, 3, 2, 3, 1]
y = [7, 2, 3, 2, 9]
# 1. ¿Cuántos elementos hay en x si se eliminan los repetidos?
print(len(set(x)))
# 2. Una lista que contenga la concatenación de ambas listas.
print(x+y)
# 3. Una lista que contenga la unión de ambas listas, sin duplicados.
print(set(x).union(set(y)))
# 4. Un conjunto que tenga la intersección de ambas listas.
print(set(x).intersection(set(y)))
# 5. Un diccionario en el que para cada entero de la lista xse almacena su cuadrado.
cuadrados_x = {num: num**2 for num in x} #chatty
dict = {}
for num in x:
    dict[num]=num**2
print(dict)
# 6. Un diccionario en el que se almacena el número de veces que cada entero aparece en la lista y.
veces_y = {num: y.count(num) for num in y}
print(veces_y)