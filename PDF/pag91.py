import random

# Crear una lista con 10 números aleatorios entre 1 y 100
numeros = [random.randint(1, 100) for _ in range(10)]
print("Lista de números:", numeros)

# 1. El mayor número de la lista
mayor = max(numeros)
print("Mayor número:", mayor)

# 2. El menor número de la lista
menor = min(numeros)
print("Menor número:", menor)

# 3. Los tres mayores números de la lista
tres_mayores = sorted(numeros, reverse=True)[:3]
print("Tres mayores números:", tres_mayores)

# 4. El mayor de los 3 primeros números de la lista
mayor_tres_primeros = max(numeros[:3])
print("Mayor de los 3 primeros números:", mayor_tres_primeros)

# 5. El menor de los 4 últimos números de la lista
menor_cuatro_ultimos = min(numeros[-4:])
print("Menor de los 4 últimos números:", menor_cuatro_ultimos)

# 6. La suma de los 5 mayores números de la lista
suma_cinco_mayores = sum(sorted(numeros, reverse=True)[:5])
print("Suma de los 5 mayores números:", suma_cinco_mayores)

# 7. La suma de los 3 menores números de la lista
suma_tres_menores = sum(sorted(numeros)[:3])
print("Suma de los 3 menores números:", suma_tres_menores)
