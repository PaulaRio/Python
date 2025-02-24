import time
from mazo import Mazo

class Blackjack:
    def __init__(self):
        self.mazo = Mazo()  # Instancia del mazo
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def repartir_cartas_iniciales(self):
        self.mazo.barajar()
        for jugador in self.jugadores:
            # Repartir dos cartas a cada jugador
            for _ in range(2):
                carta = self.mazo.repartir_carta()
                jugador.recibir_carta(carta)

    def jugar(self):
        for jugador in self.jugadores:
            if jugador.nombre != "Croupier":
                print(f"{jugador.nombre}, tu turno.")
                while jugador.calcular_puntuacion() < 21:
                    respuesta = input(f"Tu puntuación es {jugador.calcular_puntuacion()}. ¿Deseas pedir otra carta? (s/n): ")
                    if respuesta.lower() == 's':
                        carta = self.mazo.repartir_carta()
                        jugador.recibir_carta(carta)
                        print(f"Has recibido {carta}. Tu puntuación es ahora {jugador.calcular_puntuacion()}.")
                    else:
                        break
    
    def jugadaCroupier(self):
        for jugador in self.jugadores:
            if jugador.nombre == "Croupier":
                print(f"{jugador.nombre}, tu turno.")
                while jugador.calcular_puntuacion() < 16:
                    time.sleep(2)
                    carta = self.mazo.repartir_carta()
                    jugador.recibir_carta(carta)
                    print(f"Ha recibido {carta}. Tu puntuación es ahora {jugador.calcular_puntuacion()}.")
                print(f"{jugador.nombre} ha terminado su turno con una puntuación de {jugador.calcular_puntuacion()}.")


    def __str__(self):
        return "\n".join(str(jugador) for jugador in self.jugadores)

    def estado_juego(self):
        for jugador in self.jugadores:
            if jugador.calcular_puntuacion() == 21:
                print(f"{jugador.nombre} tiene un Blackjack!")
            elif jugador.calcular_puntuacion() > 21:
                print(f"{jugador.nombre} se ha pasado de 21 y ha perdido.")
            else:
                 print(f"{jugador.nombre} Tiene menos de 21 puntos y esta en partida.")

    def puntuacion_final(self):
        for jugador in self.jugadores:
            print(f"{jugador.nombre} - Puntuación Final: {jugador.calcular_puntuacion()}")

    def ganador(self):
        # Inicializar variables para el ganador
        mejor_puntuacion = 0
        ganador = None

        # Recorremos todos los jugadores
        for jugador in self.jugadores:
            puntuacion = jugador.calcular_puntuacion()
            
            # Solo consideramos jugadores cuya puntuación no haya superado 21
            if puntuacion <= 21:
                if puntuacion > mejor_puntuacion:
                    mejor_puntuacion = puntuacion
                    ganador = jugador
                elif puntuacion == mejor_puntuacion and jugador.nombre != "Croupier":
                    # Si hay empate, el jugador que no sea el croupier tiene preferencia
                    ganador = jugador

        # Si el croupier tiene la mejor puntuación y no ha superado 21, es el ganador
        croupier = next((jugador for jugador in self.jugadores if jugador.nombre == "Croupier"), None)
        if croupier:
            puntuacion_croupier = croupier.calcular_puntuacion()
            if puntuacion_croupier <= 21 and puntuacion_croupier > mejor_puntuacion:
                ganador = croupier

        # Devolvemos el ganador
        if ganador:
            print(f"El ganador es: {ganador.nombre} con una puntuación de {mejor_puntuacion}.")
        else:
            print("Nadie ha ganado. Todos han pasado de 21 o están empatados.")

