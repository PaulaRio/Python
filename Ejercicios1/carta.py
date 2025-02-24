class Carta:
    valores = {**{str(n): n for n in range(2, 11)}, "J": 10, "Q": 10, "K": 10, "A": 11}  # Añadí "A" para blackjack
    palos = ('♠', '♥', '♦', '♣')
    def __init__(self,valor,palo):
        if str(valor) not in Carta.valores:
            raise ValueError("Valor no econtrado")
        if palo not in Carta.palos:
            raise ValueError("Palo no econtrado")
        self.__palo=palo
        self.__valor=str(valor)
    
    @property
    def palo(self):
        return self.__palo
    @property
    def valor(self):
        return Carta.valores[self.__valor]
    def __str__(self):
        return f"{self.__valor}{self.__palo}"
    @palo.setter
    def palo(self,palo):
         if palo not in Carta.palos:
            raise ValueError("Palo no econtrado")
         self.__palo=palo

    @valor.setter
    def valor(self,valor):
         if valor not in Carta.valores:
            raise ValueError("Valor no econtrado")
         self.__valor=valor
    
    def __str__(self):
        return ' Carta: valor '+self.__valor + ' y palo ' + self.__palo




        


