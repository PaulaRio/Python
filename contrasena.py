'''Modulo validacion contraseñas
-Min 8 caracteres
-Minusculas, mayusculas, numeros y un un caracter no alfanumerico
-No espacios en blanco
-Valido-->return True
-No valido-->return mensaje "Contraseña no segura" '''
def validacion_pass(contrasena):
  
    num = False
    space = True
    char = False
    lenght = len(contrasena)>=8
    alfnum = False
    mayus = not contrasena.isupper()
    minus = not contrasena.islower()
   
    for ch in contrasena:
        if ch.isnumeric():
           num = True  
        elif ch.isalpha():
           char = True 
        elif ch.isspace():
           space = False
        else:
           alfnum= True
    if(num and char and lenght and alfnum and mayus and minus and space):
       print('Contraseña valida')
       return True
    else:
       return print('Contraseña no segura')
    


val = input("introduce una contraseña: ")
while( not validacion_pass(val)):
   val = input("introduce una contraseña: ")
            