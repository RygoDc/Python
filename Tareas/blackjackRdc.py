import random

def baraja():
    valores_carta = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    cartas = valores_carta * 4
    random.shuffle(cartas)
    return cartas

def valor_mano(mano):
    total= sum(mano)
    i=0
    while total > 21 and i < len(mano):
        if mano[i] == 11:
            mano[i] = 1
            total = sum(mano)
        i += 1
    return total

def blackjack():
    cartas = baraja()
    mano_jugador = []
    mano_croupier = []
    indice_carta = 0
    jugando = True

    mano_jugador.append(cartas[indice_carta])
    indice_carta += 1
    mano_croupier.append(cartas[indice_carta])
    indice_carta += 1
    mano_jugador.append(cartas[indice_carta])
    indice_carta += 1
    mano_croupier.append(cartas[indice_carta])
    indice_carta += 1

    while jugando and valor_mano(mano_jugador) <= 21:
        print(f"Tu mano es: {mano_jugador}, el total es: {valor_mano(mano_jugador)}")
        print(f"La carta del croupier es: {mano_croupier[0]}")
        respuesta = input("¿Quieres otra carta? (s/n): ")
        if respuesta.lower() == "s":
            mano_jugador.append(cartas[indice_carta])
            indice_carta += 1
        else:
            jugando = False
    
    while valor_mano(mano_croupier) < 17:
        mano_croupier.append(cartas[indice_carta])
        indice_carta += 1

    total_jugador = valor_mano(mano_jugador)
    total_croupier = valor_mano(mano_croupier)

    print(f"Tu mano final es: {mano_jugador}, el total es: {total_jugador}")
    print(f"La mano del croupier es: {mano_croupier}, el total es: {total_croupier}")

    if total_jugador > 21:
        print("Has perdido")
    elif total_croupier > 21:
        print("Has ganado")
    elif total_jugador > total_croupier:
        print("Has ganado")
    elif total_jugador < total_croupier:
        print("Has perdido")
    else:
        print("Empate")

seguir = True
while seguir:
    blackjack()
    respuesta = input("¿Quieres jugar de nuevo? (s/n): ")
    if respuesta.lower() != "s":
        seguir = False