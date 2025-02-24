class Cartas:
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    palos = ['♠', '♥', '♦', '♣']
    
    def __init__(self, valor, palo):
        if valor not in Cartas.valores:
            raise ValueError(f"Valor no válido: {valor}")
        if palo not in Cartas.palos:
            raise ValueError(f"Palo no válido: {palo}")
        self._valor = valor
        self._palo = palo
    
    def __str__(self): # ToString
        return f"{self._valor}{self._palo}"
    
    def __eq__(self, other): # equals
         return Cartas.valores.index(self._valor) == Cartas.valores.index(other.valor)
    
    def __lt__(self, other): # Less than (Menor que)
        return Cartas.valores.index(self._valor) < Cartas.valores.index(other.valor)

    def __gt__(self, other): # Greater than (Mayor que)
        return Cartas.valores.index(self._valor) > Cartas.valores.index(other.valor)
    
    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor not in Cartas.valores:
            raise ValueError(f"Valor no válido: {valor}")
        self._valor = valor

    @property
    def palo(self):
        return self._palo

    @palo.setter
    def palo(self, palo):
        if palo not in Cartas.palos:
            raise ValueError(f"Palo no válido: {palo}")
        self._palo = palo