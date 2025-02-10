import random

# Variables de puntuación inicial
victorias_jugador = 0
derrotas_jugador = 0
victorias_jugador2 = 0
derrotas_jugador2 = 0
victorias_cpu = 0
derrotas_cpu = 0

# Diccionarios de coordenadas de letras
letras_columnas = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}


def convertir_coordenadas(barcos):
    return [(fila, letras_columnas[columna]) for fila, columna in barcos]
"""
    Convierte las coordenadas numéricas de los barcos a coordenadas con letras.

    Args:
    barcos: Lista de tuplas con las coordenadas numéricas (fila, columna).

    Returns:
    Lista de tuplas con coordenadas (fila, letra).
    """


def crear_tablero():
    return [['~' for _ in range(5)] for _ in range(5)]
"""
    Crea un tablero de juego de 5x5 con el  agua asi: ('~').

    Returns:
    Lista de listas representando el tablero de juego.
    """

def mostrar_tablero(tablero, ocultar):
    print("  A B C D E")
    fila_numero = 0
    for fila in tablero:
        print(fila_numero, end=' ')
        for celda in fila:
            if ocultar == 1 and celda == '⛵':
                print('~', end=' ')
            else:
                print(celda, end=' ')
        print()
        fila_numero += 1
"""
    Muestra el tablero en la consola.

    Args:
    tablero: Matriz de 5x5 que representa el tablero.
    ocultar: Indica si los barcos deben mostrarse (0) o no (1).
    """

def obtener_cantidad_barcos():
    cantidad = 0
    while cantidad < 1 or cantidad > 5:
        entrada = input("¿Cuántos barcos deseas colocar? (1-5): ")
        if entrada.isdigit():
            cantidad = int(entrada)
        if cantidad < 1 or cantidad > 5:
            print("Opción inválida. Ingresa un número entre 1 y 5, por favor.")
    return cantidad
"""
       Solicita al usuario la cantidad de barcos a colocar.

       Returns:
       Entero entre 1 y 5 representando la cantidad de barcos.
       """



def colocar_barcos(tablero, cantidad):
    barcos = []
    while len(barcos) < cantidad:
        fila, columna = random.randint(0, 4), random.randint(0, 4)
        if tablero[fila][columna] == '~':
            tablero[fila][columna] = '⛵'
            barcos.append((fila, columna))
    return barcos
"""
   Coloca barcos aleatoriamente en el tablero.

   Args:
   tablero: Matriz de 5x5 representando el tablero de juego.
   cantidad: Cantidad de barcos a colocar.

   Returns:
   Lista de coordenadas donde se colocaron los barcos.
   """


def obtener_fila():
    numero = -1
    while numero < 0 or numero > 4:
        entrada = input("Ingresa fila (0-4): ")
        if entrada.isdigit():
            numero = int(entrada)
        if numero < 0 or numero > 4:
            print("Opción inválida. Ingresa un número entre 0 y 4, por favor.")
    return numero
"""
    Solicita al usuario una fila válida entre 0 y 4.

    Returns:
    Entero representando la fila seleccionada.
    """

def obtener_columna():
    letras = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
    columna = None
    while columna is None:
        entrada = input("Ingresa la columna de: (A-E): ").lower()
        if entrada in letras:
            columna = letras[entrada]
        else:
            print("Opción inválida. Ingresa una letra entre A y E, por favor.")
    return columna
"""
   Solicita al usuario una columna válida entre A y E.

   Returns:
   Entero representando la columna seleccionada.
   """

def mostrar_tablero_con_barcos(tablero, barcos):
    for fila, columna in barcos:
        tablero[fila][columna] = '⛵'
    mostrar_tablero(tablero, ocultar=0)


def actualizar_resultados(victorias_jugador, derrotas_jugador, victorias_cpu, derrotas_cpu, resultado):
    if resultado == 'jugador':
        victorias_jugador += 1
    elif resultado == 'cpu':
        victorias_cpu += 1
    else:
        derrotas_jugador += 1
        derrotas_cpu += 1
    return victorias_jugador, derrotas_jugador, victorias_cpu, derrotas_cpu


def jugar_contra_pc():
    print("Modo: Contra la PC")
    tablero_jugador = crear_tablero()
    tablero_cpu = crear_tablero()
    num_barcos = obtener_cantidad_barcos()
    barcos_cpu = colocar_barcos(tablero_cpu, num_barcos)
    intentos = 5
    barcos_restantes = num_barcos

    print("\n¡Es momento de adivinar los barcos enemigos!")

    while intentos > 0 and barcos_restantes > 0:
        print("\nTu tablero:")
        mostrar_tablero(tablero_jugador, 1)

        fila = obtener_fila()
        columna = obtener_columna()

        if tablero_jugador[fila][columna] != '~':
            print("Ya disparaste aquí. Intenta otra vez, por favor.")
        else:
            if (fila, columna) in barcos_cpu:
                print("¡Tocado y hundido!")
                tablero_jugador[fila][columna] = '⛵'
                barcos_restantes -= 1
            else:
                print("Aguaaaaa!")
                tablero_jugador[fila][columna] = 'X'
            intentos -= 1

    if barcos_restantes > 0:
        print("¡Perdiste! Los barcos estaban en:", convertir_coordenadas(barcos_cpu))
        print("🏆🏆 Ganador: CPU 🏆🏆")
    else:
        print("¡Ganaste! Hundiste todos los barcos.")
        print("🏆🏆 Ganador: Jugador 🏆🏆")

    print("\nAquí están las posiciones finales de los barcos:")
    mostrar_tablero_con_barcos(tablero_cpu, barcos_cpu)
    volver_a_jugar("pc")


def jugar_contra_jugador():
    puntajes = {"victorias_j1": 0, "derrotas_j1": 0, "victorias_j2": 0, "derrotas_j2": 0}

    print("Modo: Contra otro jugador")
    tablero_jugador1 = crear_tablero()
    tablero_jugador2 = crear_tablero()
    num_barcos = obtener_cantidad_barcos()
    barcos_jugador1 = colocar_barcos(tablero_jugador1, num_barcos)
    barcos_jugador2 = colocar_barcos(tablero_jugador2, num_barcos)
    intentos = 5
    barcos_restantes_j1 = num_barcos
    barcos_restantes_j2 = num_barcos

    print("\n¡Es momento de adivinar los barcos enemigos!")

    while intentos > 0 and (barcos_restantes_j1 > 0 and barcos_restantes_j2 > 0):
        print("\nTurno del Jugador 1:")
        mostrar_tablero(tablero_jugador2, 1)

        fila = obtener_fila()
        columna = obtener_columna()

        if tablero_jugador2[fila][columna] == '~':
            if (fila, columna) in barcos_jugador2:
                print("¡Tocado y hundido!")
                tablero_jugador2[fila][columna] = '⛵'
                barcos_restantes_j2 -= 1
            else:
                print("Aguaaaaa!")
                tablero_jugador2[fila][columna] = 'X'
        else:
            print("Ya disparaste aquí.")

        if barcos_restantes_j2 == 0:
            print("🏆🏆 Ganador: Jugador 1 🏆🏆")
            break

        print("\nTurno del Jugador 2:")
        mostrar_tablero(tablero_jugador1, 1)

        fila = obtener_fila()
        columna = obtener_columna()

        if tablero_jugador1[fila][columna] == '~':
            if (fila, columna) in barcos_jugador1:
                print("¡Tocado y hundido!")
                tablero_jugador1[fila][columna] = '⛵'
                barcos_restantes_j1 -= 1
            else:
                print("Aguaaaaa!")
                tablero_jugador1[fila][columna] = 'X'
        else:
            print("Ya disparaste aquí.")

        if barcos_restantes_j1 == 0:
            print("🏆🏆 Ganador: Jugador 2 🏆🏆")
            break

        intentos -= 1

    print("\nAquí están las posiciones finales de los barcos:")

    print("\nLos barcos del Jugador 1 estaban en:", convertir_coordenadas(barcos_jugador1))
    print("Tablero final del Jugador 1:")
    mostrar_tablero_con_barcos(tablero_jugador1, barcos_jugador1)

    print("\nLos barcos del Jugador 2 estaban en:", convertir_coordenadas(barcos_jugador2))
    print("Tablero final del Jugador 2:")
    mostrar_tablero_con_barcos(tablero_jugador2, barcos_jugador2)

    volver_a_jugar("jugadores")  # Llamar al menú de volver a jugar


def volver_a_jugar(modo):
    opcion = ""
    while opcion != '1' and opcion != '2':
        print("\n¿🎮🎮Quieres volver a jugar🎮🎮?")
        print("1. Sí")
        print("2. No (Salir)")
        opcion = input("Selecciona una opción (1 o 2): ")
        if opcion == '1':
            jugar()
        elif opcion == '2':
            print("🎮🎮Gracias por jugar🎮🎮. ¡Hasta la próxima!")
            return


def jugar():
    opcion = ""
    while opcion != '1' and opcion != '2':
        print("Bienvenido a Batalla Naval")
        print("Selecciona un modo de juego:")
        print("1. Jugar contra la CPU")
        print("2. Jugar contra otro jugador")
        opcion = input("Selecciona una opción (1 o 2): ")

        if opcion == '1':
            jugar_contra_pc()
        elif opcion == '2':
            jugar_contra_jugador()
        else:
            print("Opción inválida. Inténtalo de nuevo.")

jugar()


