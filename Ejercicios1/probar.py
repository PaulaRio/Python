from carta import Carta
cartas = [Carta(valor, palo) for palo in Carta.palos for valor in Carta.valores.keys()]

for carta in cartas:
    print(carta)