cadena = "Cabeza grande, ojos hermosos"
# a) El tamaño de la cadena
tamano = len(cadena)
print("a) El tamaño de la cadena:", tamano)

# b) Los primeros cinco caracteres de la cadena
primeros_cinco = cadena[:5]
print("b) Los primeros cinco caracteres:", primeros_cinco)

# c) Los siete últimos caracteres
ultimos_siete = cadena[-7:]
print("c) Los siete últimos caracteres:", ultimos_siete)

# d) Los cinco primeros caracteres, de dos en dos
de_dos_en_dos = cadena[:5:2]
print("d) Los cinco primeros caracteres, de dos en dos:", de_dos_en_dos)

# e) Los últimos trece caracteres, de tres en tres
de_tres_en_tres = cadena[-13::3]
print("e) Los últimos trece caracteres, de tres en tres:", de_tres_en_tres)

# f) En mayúscula, los caracteres en posiciones múltiplo de tres
mayusculas_multiplo_tres = ''.join([cadena[i].upper() for i in range(len(cadena)) if i % 3 == 0])
print("f) Caracteres en posiciones múltiplo de tres en mayúscula:", mayusculas_multiplo_tres)

# g) De dos en dos, del carácter en la posición 4 al de la 17
de_dos_en_dos_4_17 = cadena[4:18:2]
print("g) De dos en dos, del carácter en la posición 4 al de la 17:", de_dos_en_dos_4_17)

# h) ¿Está el carácter "x" en la cadena?
print("h) ¿Está el carácter 'x' en la cadena?", "x" in cadena)

# i) ¿Y "o", en mayúscula o minúscula?
esta_o = "o" in cadena.lower()  # Convertimos toda la cadena a minúsculas para buscar "o"
print("i) ¿Está el carácter 'o' en la cadena (en mayúscula o minúscula)?", esta_o)

