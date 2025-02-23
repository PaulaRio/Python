import random
from carta import Carta
class Mazo:

    def __init__(self):
        self.cartas=[]
        for p in Carta.palo:
            for v in Carta.valor:
               self.cartas.append(Carta(v,p))
    
    
    def repartir_carta(self):
        if self.cartas:
           return self.cartas.pop() 
        else:
            None
    
    def barajar(self):
        random.shuffle(self.cartas)



        


