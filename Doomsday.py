#Del año sacamos la centuria y de los dos ultimos digitos el multiplo de 12 mas cercano por debajo, el resto, y el cociente de 4 de ese resto, se suman los 3 digitos
#A ese digito se le suma el numero correspondiente a la centuria
#Tuplas
fechas=(3,28,14,4,9,6,11,8,5,10,7,12) #Equivalente a cada mes, cuando sepas el mes buscas el dia correspondiente
centurias=(2,0,5,3) 
dias=('domingo','lunes','martes','miercoles','jueves','viernes','sabado')
meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
#Datos de entrada
d = int(input("Ingresa el día: "))
m = int(input("Ingresa el mes: "))
a = int(input("Ingresa el año: "))
#Calculo centuria
centuria= a //100*100
#Extraemos la terminacion
terminacion = a - centuria

#Calculo cociente resto modulo 12
dia = sum(divmod(terminacion,12))

#Añadimos bisiestos de ser el caso
dia += terminacion %12 // 4

#Añadimos valor de la centuria
dia+= centurias [centuria % 400 //100]

bisiesto=(a %4 == 0) and (a % 100 !=0 or a % 400 == 0)
#Añadimos diferencia con la fecha de referencia
if bisiesto and m in [1,2]:
    dia +=d-(fechas[m-1]+1)
else:
    dia+= d -fechas[m-1]

#Calculamos módulo 7
dia %=7
#Presentamos mensaje de salida
print(f'El dia {d} de {meses[m-1]} de {a} es {dias[dia]}')