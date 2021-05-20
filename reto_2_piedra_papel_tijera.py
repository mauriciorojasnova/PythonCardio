def run():
    partidas = 3
    contador_jugador_1 = 0
    contador_jugador_2 = 0

    while partidas > 0:
        jugador_1 = input("Jugador 1, escoge piedra, papel o tijeras: ")
        jugador_2 = input("Jugador 2, escoge piedra, papel o tijeras: ")

        if jugador_1 == jugador_2:
            print(f"Los dos jugadores escogieron {jugador_1}, hay un empate.\n")
        elif (jugador_1 == "piedra" and jugador_2 == "tijeras") or (jugador_1 == "tijeras" and jugador_2 == "papel") or (jugador_1 == "papel" and jugador_2 == "piedra"):
            print("El jugador 1 ha ganado esta ronda.\n")
            contador_jugador_1 += 1
        else:
            print("El jugador 2 ha ganado esta ronda.\n")
            contador_jugador_2 += 1
        partidas -= 1
    
    if contador_jugador_1 > contador_jugador_2:
        print("El ganador de la partida fue el jugador 1.")
    elif contador_jugador_1 < contador_jugador_2:
        print("El ganador de la partida fue el jugador 2.")
    else:
        print("La partida terminó en empate.")



if __name__ == "__main__":
    print(""" 
    Bienvenido al juego de piedra, papel o tijeras.
    El ganador de la partida será el que tenga más puntos al finalizar las tres rondas.
    """)
    run()