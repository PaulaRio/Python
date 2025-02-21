class Mascota:
    def __init__(self):
        self.__nombre=input('introduce un nombre: ')
        self.__edad=input('introduce una edad: ')

    def mostrar(self):
        print('Nombre: '+ self.nombre)
        print('Edad: '+ self.edad)
    
    def __str__(self):
        return ' La mascota se llama '+self.__nombre + 'y tiene ' + self.edad

class Gato(Mascota):
    def __init__(self):
        super().__init__()
        self.peso=float(input('El peso del gato es'))

    def mostrar(self):
        super().mostrar()
        print('Peso ', self.peso)

    def dieta(self):
        if self.peso > 8:
            print(f'El gato {self.nombre} necesita ponerse a dieta')
        else:
            print(f'El gato {self.nombre} esta dentro del peso')


class Alumno:
    def __init__(self):
        self.nombre=input('Introduce el nombre')
        self.nota=float(input('Introduce la nota'))

    def imprimir(self):
        return '(' +(self.nombre)+ ','+ str(self.nota)+ ')'
    
    def notas(self):
        if self.nota>=5:
            print(f'El alumno {self.nombre} esta aprobado')


