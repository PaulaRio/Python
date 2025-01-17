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