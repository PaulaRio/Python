from cartas import Cartas

class Mazo:
    def __init__(self):

        self.cartas = []
        for valor in Cartas.valores:
            for palo in Cartas.palos:
                self.cartas.append(Cartas(valor, palo))
    
    def __str__(self):
        return ", ".join([str(carta) for carta in self.cartas])

    def repartir_carta(self):
        if self.cartas:
            return self.cartas.pop()
        else:
            return None

    def barajar(self):
        import random
        random.shuffle(self.cartas)