import random
from carta import Carta
class Mazo:

    def __init__(self):
        self.cartas=[]
        for p in Carta.palos:
            for v in Carta.valores.keys():
               self.cartas.append(Carta(v,p))
        self.barajar()
    
    
    def repartir_carta(self):
        if self.cartas:
           return self.cartas.pop() 
        else:
            None
    
    def barajar(self):
        random.shuffle(self.cartas)



        


