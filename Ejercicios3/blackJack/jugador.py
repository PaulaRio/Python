from carta import Carta
from mazo import Mazo
class Jugador:
    def __init__(self,nombre):
        self.nombre=nombre
        self.mano=[]
    
    @property
    def nombre(self):
        return self.nombre
    @nombre.setter
    def nombre(self,nombre):
         self.nombre=nombre

    def recibir_carta(self,mazo):
       self.mano.append(mazo.repartir_carta)

    def calcular_puntuacion(self):
        

      
    
   




        


