
import math


class Triangulo:
    def __init__(self):
        self.a=int(input('Introduce el primer lado del triangulo '))
        self.b=int(input('Introduce el segundo lado del triangulo '))
        self.c=int(input('Introduce el tercer lado del triangulo '))
    
    def imprimir(self):
        return 'lado: '+ str(self.a) + '\nlado b: '+  str(self.b) + '\nlado c: '+  str(self.c) 

    def tipo(self):
        if self.a==self.b and self.a==self.c:
            return 'equilatero'
        elif  self.a==self.b or self.a==self.c or self.b==self.c:
            return 'isosceles'
        else:
            return 'escaleno'
    
    def area(self):
        self.semiperimetro= (self.a + self.b + self.c)/2
        self.superficie = math.sqrt(self.semiperimetro*(self.semiperimetro-self.a)*(self.semiperimetro-self.b)*(self.semiperimetro-self.c))
        return self.superficie

triangulo= Triangulo()
print(triangulo.tipo())
print(f'El area del triangulo es {triangulo.area()}')

