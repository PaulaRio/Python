'''Programa que calcula el día de la semana dada una fecha
introducida por el usuario.
Implementa el algoritmo utilizado para realizar el cálculo mental
descrito en https://youtu.be/z2x3SSBVGJU?feature=shared
'''

#Cargamos datos necesarios en tuplas
fechas = (3,28,14,4,9,6,11,8,5,10,7,12)
centurias = (2,0,5,3)
dias = ('domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado')
meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

#Recogemos datos de entrada
d = int(input('Introduce el día: '))
m = int(input('Introduce el mes: '))
a = int(input('Introduce el año: '))

#Realizamos cálculo

#Calculamos la centuria
centuria = a // 100 * 100

#Extraemos terminacion del año
terminacion = a - centuria

#Calculamos cociente y resto módulo 12
dia = sum(divmod(terminacion, 12))

#Añadimos bisiestos, si los hubiera
dia += terminacion % 12 // 4

#Añadimos valor de la centuria
dia += centurias[centuria % 400  // 100]

#Comprobamos si el año es bisiesto
bisiesto = (a % 4 == 0) and (a % 100 != 0 or a % 400 == 0)

#Añadimos diferencia con la fecha de referencia
if bisiesto and m in range(1,3):
    dia += d - (fechas[m-1] + 1) 
else:
    dia += d - fechas[m-1]

#Calculamos módulo 7
dia %= 7

#Presentamos mensaje de salida
print(f'El {d} de {meses[m-1]} de {a} es {dias[dia]}')