from carta import Carta
from mazo import Mazo
class Jugador:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.mano=[]
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
         self.__nombre=nombre

    def recibir_carta(self,mazo):
       self.mano.append(mazo.repartir_carta)

    def limpiar_mano(self):
    
        self.mano.clear()  

    def calcular_puntuacion(self):
        puntuacion = 0
        as_count = 0
        for carta in self.mano:
            if carta.valor in ['J', 'Q', 'K']:
                puntuacion += 10
            elif carta.valor == 'A':
                puntuacion += 1
                ascount += 1
            else:
                puntuacion += int(carta.valor)

        # Ajustar el valor de los Ases si es posible (1 o 11)
        for _ in range(as_count):
            if puntuacion + 10 <= 21:
                puntuacion += 10

        return puntuacion
    def mostrar_mano(self):
        return ", ".join(str(carta) for carta in self.mano)
    
    def __str__(self):
        return f"Jugador: {self.__nombre}\nMano: {self.mostrar_mano()}\nPuntuación: {self.calcular_puntuacion()}"
    def __eq__(self, otro):
        return self.calcular_puntuacion() == otro.calcular_puntuacion()

    def __lt__(self, otro):
        return self.calcular_puntuacion() < otro.calcular_puntuacion()

    def __gt__(self, otro):
        return self.calcular_puntuacion() > otro.calcular_puntuacion()


      
    
   




        


