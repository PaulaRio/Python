class Jugador:
    def __init__(self, nombre):
        self._nombre = nombre
        self.mano = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre.strip():
            raise ValueError("El nombre del jugador no puede estar vacío.")
        self._nombre = nombre

    def recibir_carta(self, carta):
        self.mano.append(carta)

    def calcular_puntuacion(self):
        puntuacion = 0
        as_count = 0
        for carta in self.mano:
            if carta.valor in ['J', 'Q', 'K']:
                puntuacion += 10
            elif carta.valor == 'A':
                puntuacion += 1
                as_count += 1
            else:
                puntuacion += int(carta.valor)

        # Ajustar el valor de los Ases si es posible (1 o 11)
        for _ in range(as_count):
            if puntuacion + 10 <= 21:
                puntuacion += 10

        return puntuacion

    def mostrar_mano(self):
        return ', '.join(str(carta) for carta in self.mano)
    
    def mostrar_mano_croupier(self):
        if self.mano:
            return str(self.mano[0])
        return "Sin cartas"
    
    def mostrar_mano_croupier_segunda_carta(self):
        if self.mano:
            return str(self.mano[1])
        return "Sin cartas"

    def limpiar_mano(self):
        self.mano.clear()

    def __str__(self):
        return f"{self.nombre} - Cartas: {self.mostrar_mano()}, Puntuación: {self.calcular_puntuacion()}"

    def __eq__(self, otro):
        return self.calcular_puntuacion() == otro.calcular_puntuacion()

    def __lt__(self, otro):
        return self.calcular_puntuacion() < otro.calcular_puntuacion()

    def __gt__(self, otro):
        return self.calcular_puntuacion() > otro.calcular_puntuacion()
