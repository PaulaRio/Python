x = 101  # Valor inicial

# a) Comprobar si x es 42
if x == 42:
    print("Sentido de la vida encontrado")
else:
    print("Sigue buscando")

# b) Si x es menor que 100, imprimirlo e incrementarlo en 1
if x < 100:
    print(x)
    x += 1

# c) Si no (es decir, si x es 100 o más), actualizar su valor al cuadrado
else:
    x = x ** 2
    print(x)

# d) Si es mayor que 0 y par, imprimir "exacto"
if x > 0 and x % 2 == 0:
    print("Exacto")
# e) Si no, actualizar su valor a su mitad
else:
    x = x / 2
    print(x)

# f) Si es mayor que 0, impar y menor o igual que 365, imprimir "podría ser un día"
if x > 0 and x % 2 == 1 and x <= 365:
    print("Podría ser un día")
else:
    print("No lo es")

# g) Si el número es diferente de cero, imprimir "algo es algo"
if x != 0:
    print("Algo es algo")

# h) Si el número es cero, asignarle el valor 100
if x == 0:
    x = 100
