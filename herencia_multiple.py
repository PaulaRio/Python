class Estudiante:
    def __init__(self):
        self.edad=int(input('Que edad tienes: '))
        self.nombre=input('Cual es tu nombre: ')
class Instituto:
    def preinscripcionInstituto(self,estudios,instituto):
        self.estudios=estudios
        self.instituto=instituto

class Estudios(Estudiante, Instituto):
    def presentacion(self):
        print(f'me llamo {self.nombre}, tengo {self.edad} años ')
        print(f'y quiero  estudiar {self.estudios} en el instituto {self.instituto}')

paco = Estudios()
paco.preinscripcionInstituto('DAM', 'IESComercio')
paco.presentacion
        
