import time
from jugador import Jugador
from blackjack import Blackjack

# Crear la instancia del juego
partida = Blackjack()

# Agregar jugador principal
nombre_jugador = input("Bienvenido a la mesa, jugador: ")
jugador_principal = Jugador(nombre_jugador)
partida.agregar_jugador(jugador_principal)

# Pedir número de jugadores adicionales
while True:
    try:
        players = int(input("¿Cuántos jugadores quieres que haya (2-5)?: "))
        if 2 <= players <= 5:
            break
        else:
            print("Número no válido. Ingresa un número entre 2 y 5.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Agregar jugadores adicionales
for i in range(players - 1):  # Restamos 1 porque ya está el jugador principal
    jugador_nuevo = Jugador(f"Jugador {i+1}")
    partida.agregar_jugador(jugador_nuevo)

# Agregar al croupier
croupier = Jugador("Croupier")
partida.agregar_jugador(croupier)

# Iniciar el bucle del juego
while True:
    # Iniciar la partida
    input("\nPresiona Enter para empezar la partida...")

    # Limpiar las manos de los jugadores antes de repartir nuevas cartas
    for jugador in partida.jugadores:
        jugador.limpiar_mano()

    # Repartir cartas iniciales
    partida.repartir_cartas_iniciales()

    # Mostrar las cartas iniciales de cada jugador
    print("\nCartas iniciales de cada jugador:")
    for jugador in partida.jugadores:
        if jugador.nombre != "Croupier":
            print(f"{jugador.nombre}: {jugador.mostrar_mano()} (Puntuación: {jugador.calcular_puntuacion()})")

    # Mostrar la carta inicial del croupier
    print("\nCarta inicial del Croupier:")
    for jugador in partida.jugadores:
        if jugador.nombre == "Croupier":
            print(jugador.mostrar_mano_croupier())

    print("\n--- Inicia el turno de los jugadores ---\n")

    # Iniciar el juego
    partida.jugar()

    # Iniciar el turno del croupier
    print("\n--- Turno del Croupier ---\n")
     # Mostrar la segunda carta inicial del croupier
    print("Segunda carta inicial del Croupier:")
    time.sleep(2)
    for jugador in partida.jugadores:
        if jugador.nombre == "Croupier":
            print(jugador.mostrar_mano_croupier_segunda_carta())
            print("El croupier acumula: ",jugador.calcular_puntuacion())
    time.sleep(2)
    partida.jugadaCroupier()

    time.sleep(2)
    # Mostrar estado final de la partida
    print("\nCartas finales de cada jugador:")
    for jugador in partida.jugadores:
        print(f"{jugador.nombre}: {jugador.mostrar_mano()} (Puntuación: {jugador.calcular_puntuacion()})")

    time.sleep(2)
    print("\n--- Estado del Juego ---\n")
    partida.estado_juego()

    time.sleep(2)

    print("\n--- Puntuación Final ---\n")
    partida.puntuacion_final()

    time.sleep(2)

    print("\n--- Ganador ---\n")
    partida.ganador()

    # Preguntar si desean jugar otra partida
    respuesta = input("\n¿Jugar otra partida? (s/n): ")
    if respuesta.lower() != 's':
        break  # Salir del bucle si la respuesta es no
