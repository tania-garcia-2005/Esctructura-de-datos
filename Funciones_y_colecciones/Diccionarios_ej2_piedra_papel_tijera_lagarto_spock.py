from random import choice  # Importa la función choice para seleccionar de manera aleatoria
# Mi portada.
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓Fecha: 24 de Noviembre de 2024     🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print()
print("----------------------------------------------------------------------------------")

# Constantes para las opciones del juego y los posibles resultados.
OPCION_PIEDRA = "Piedra"
OPCION_PAPEL = "Papel"
OPCION_TIJERAS = "Tijeras"
LAGARTO = "Lagarto"
SPOCK = "Spock"
JUGADOR = "Jugador"
EMPATE = "Empate"
CPU = "CPU"

# Función para mostrar mi menú.
def menu():
    print("1) Piedra.")
    print("2) Papel.")
    print("3) Tijera.")
    print("4) Lagarto.")
    print("5) Spock.")
    print("6) Ver las reglas.")
    print("0) Salir.")
    print()
    opcion = int(input("Ingrese una opción: "))  # El usuario ingresa su opción
    return opcion

# Función para que el jugador y la CPU elijan sus opciones.
def jugar(opcion):
    if opcion == 1:
        eleccion_usuario = OPCION_PIEDRA
    elif opcion == 2:
        eleccion_usuario = OPCION_PAPEL
    elif opcion == 3:
        eleccion_usuario = OPCION_TIJERAS
    elif opcion == 4:
        eleccion_usuario = LAGARTO
    elif opcion == 5:
        eleccion_usuario = SPOCK
    else:
        eleccion_usuario = None

    # La CPU elige una opción aleatoriamente.
    eleccion_cpu = choice([OPCION_PIEDRA, OPCION_PAPEL, OPCION_TIJERAS, LAGARTO, SPOCK])
    return eleccion_usuario, eleccion_cpu

# Diccionario con las reglas del juego.
reglas_del_juego = {
    (OPCION_PIEDRA, OPCION_TIJERAS): JUGADOR,
    (OPCION_PIEDRA, OPCION_PAPEL): CPU,
    (OPCION_TIJERAS, OPCION_PAPEL): JUGADOR,
    (OPCION_TIJERAS, OPCION_PIEDRA): CPU,
    (OPCION_PAPEL, OPCION_PIEDRA): JUGADOR,
    (OPCION_PAPEL, OPCION_TIJERAS): CPU,
    (OPCION_PIEDRA, LAGARTO): JUGADOR,
    (LAGARTO, OPCION_PIEDRA): CPU,
    (LAGARTO, SPOCK): JUGADOR,
    (SPOCK, LAGARTO): CPU,
    (SPOCK, OPCION_TIJERAS): JUGADOR,
    (OPCION_TIJERAS, SPOCK): CPU,
    (OPCION_TIJERAS, LAGARTO): JUGADOR,
    (LAGARTO, OPCION_TIJERAS): CPU,
    (LAGARTO, OPCION_PAPEL): JUGADOR,
    (OPCION_PAPEL, LAGARTO): CPU,
    (OPCION_PAPEL, SPOCK): JUGADOR,
    (SPOCK, OPCION_PAPEL): CPU,
    (SPOCK, OPCION_PIEDRA): JUGADOR,
    (OPCION_PIEDRA, SPOCK): CPU,
}

# Variables para llevar el conteo de victorias, empates y derrotas.
victorias_jugador = 0
victorias_cpu = 0
empates = 0

# Imprime el título del juego.
print("╏╠══[𝍖𝍖𝍖 𝙹𝚞𝚎𝚐𝚘 𝚍𝚎 𝙿𝚒𝚎𝚍𝚛𝚊, 𝙿𝚊𝚙𝚎𝚕, 𝚃𝚒𝚓𝚎𝚛𝚊𝚜, 𝙻𝚊𝚐𝚊𝚛𝚝𝚘, 𝚂𝚙𝚘𝚌𝚔 𝍖𝍖𝍖]      💦")

opcion = None
while opcion != 0:
    # Muestra el menú y obtiene la opción del jugador.
    opcion = menu()

    # opción ingresada.
    if opcion < 0 or opcion > 6:
        print("La opción no es válida. Por favor, ingrese un número entre 0 y 6.")
        print()
    elif opcion == 6:
        # Muestra las reglas del juego.
        print("""╏╠══[𝍖𝍖𝍖 𝚁𝚎𝚐𝚕𝚊𝚜 𝍖𝍖𝍖]      💦:
        - Tijeras cortan papel.
        - Papel cubre piedra.
        - Piedra aplasta lagarto.
        - Lagarto envenena Spock.
        - Spock destruye tijeras.
        - Tijeras decapitan lagarto.
        - Lagarto come papel.
        - Papel desaprueba Spock.
        - Spock vaporiza piedra.
        - Piedra aplasta tijeras.
        La CPU elige una opción aleatoriamente.""")
        print()
    elif opcion == 0:#si presiona cero.
        # Salir del juego.
        print("Usted ha salido exitosamente del juego. ¡Gracias por jugar!")
    else:
        # Jugar una partida(ronda).
        eleccion_usuario, eleccion_cpu = jugar(opcion)

        # Mostrar las elecciones del jugador y la CPU.
        print(f"\nJugador eligió: {eleccion_usuario}")
        print(f"CPU eligió: {eleccion_cpu}")
        print()

        # Calcula el resultado del juego según las reglas establecidas.
        resultado = reglas_del_juego.get((eleccion_usuario, eleccion_cpu), EMPATE)

        if resultado == JUGADOR:
            victorias_jugador += 1
            print("El ganador es: el Jugador")
        elif resultado == CPU:
            victorias_cpu += 1
            print("El ganador es: la CPU")
        else:
            empates += 1
            print("¡WOW!,es un: EMPATE")

        # Muestra el total de los resultados.
        print(f"Victorias del Jugador: {victorias_jugador}, Victorias de la CPU: {victorias_cpu}, Empates: {empates}")
        print()
