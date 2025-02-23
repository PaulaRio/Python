class operaciones_basicas:
  def __init__(self):
    pass 
  def suma(self,a,b):
    return a+b
  def resta(self,a,b):
    return a-b
  def multiplicacion(self,a,b):
    return a*b
  def division(self,a,b):
    if(b==0):
       raise ZeroDivisionError("ERROR: No se puede dividir por cero")
    return a/b


 