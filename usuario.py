'''Modulo validacion nombres de usuario
-6 a 12 caracteres
-Caracteres alfanumericos
-Mostrar mensaje error
-Valido-->return True'''
def validacion_user(contrasena):
  
    num = False
    space = False
    char = False
    min_lenght = len(contrasena)>=6
    max_lenght = len(contrasena)<=12
    alfnum = False
    
      
    for ch in contrasena:
       if ch.isnumeric():
         num = True  
       elif ch.isalpha():
         char = True 
       elif ch.isspace():
         space = True
       else:
         alfnum= True
    if(not min_lenght):
     print('Nombre usuario menor de 6 caracteres')
    if(not max_lenght):
     print('Nombre usuario mayor de 12 caracteres')
    if(not char)                  :
      print('Debe contener letras')  
    if(space):
      print('No debe contener espacios')  
    if(num or alfnum):
      print('No debe contener numeros ni caracteres especiales')                                                                                                         
    if(min_lenght and max_lenght and char and not space and not num and not alfnum):
      print('Usuario valido')
      return True
    

val = input("Introduce un nombre de usuario: ")
while( not validacion_user(val)):
  val = input("Introduce un nombre de usuario: ")