class calculadora_class:
  def __init__(self):
    pass 
  def suma(self,a,b):
    print(f'El resultado de la suma',a+b)
    return a+b
  def resta(self,a,b):
    print(f'El resultado de la resta', a-b)
    return a-b
  def multiplicacion(self,a,b):
    print(f'El resultado de la multiplicacion', a*b)
    return a*b
  def division(self,a,b):
    if(b==0):
        print('No se puede dividir entre 0')
        return
    else:
        print(f'El resultado de la division', a/b)
    return a/b
 