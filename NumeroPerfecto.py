def divisores(n):
    divisores = []
    for i in range(1, n+1):
        if n % i == 0:
            divisores.append(i)
    return divisores

def perfecto(n):

    if sum(divisores(n))==2*n:
       return n 

lista_perfectos = []
for numero in range(1,1001):
    variable=perfecto(numero)
    if variable:
        lista_perfectos.append(variable)

print(lista_perfectos)