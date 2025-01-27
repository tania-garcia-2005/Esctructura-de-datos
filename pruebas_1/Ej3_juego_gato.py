# ------------------------ Juego Gato ------------------------

def crear_tablero_gato():
    """
    Crea un tablero vacío para el juego del Gato (3x3).

    Returns:
     Una matriz 3x3 inicializada con espacios en blanco.
    """
    # Crea una matriz 3x3 con espacios vacíos
    return [[' ' for _ in range(3)] for _ in range(3)]


def mostrar_tablero_gato(tablero):
    """
    Muestra el tablero del juego del Gato en formato legible.

    Args:
    tablero: Matriz 3x3 que representa el estado actual del tablero.
    """
    # Recorre cada fila del tablero
    for fila in tablero:
        # Imprime los elementos de la fila separados por barras
        print(fila[0] + '|' + fila[1] + '|' + fila[2])
        # Imprime una línea divisoria entre filas
        print('-' * 5)


def verificar_victoria_gato(tablero, jugador):
    """
    Verifica si el jugador actual ha ganado el juego.
    Evalúa líneas horizontales, verticales y diagonales.

    Args:
    tablero: Matriz 3x3 que representa el estado del tablero.
    jugador: Símbolo del jugador ('X' o 'O').

    Returns:
    bool: True si el jugador ha ganado, False en caso contrario.
    """
    # Verifica filas y columnas
    for i in range(3):
        # Verifica filas
        if tablero[i][0] == jugador and tablero[i][1] == jugador and tablero[i][2] == jugador:
            return True
        # Verifica columnas
        if tablero[0][i] == jugador and tablero[1][i] == jugador and tablero[2][i] == jugador:
            return True

    # Verifica la diagonal principal
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    # Verifica la diagonal secundaria
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True

    # Si no hay victoria, retorna False
    return False


def cpu_jugar_gato(tablero):
    """
    Selecciona un movimiento para la CPU de forma sencilla:
    elige el primer espacio vacío disponible.

    Args:
    tablero: Matriz 3x3 que representa el estado actual del tablero.

    Returns:
    tuple: Coordenadas (fila, columna) del movimiento de la CPU.
    """
    # Busca el primer espacio vacío en el tablero
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == ' ':
                return fila, columna
    # Retorna un valor inválido si no hay espacios disponibles (no debería ocurrir)
    return -1, -1


def jugar_gato(es_contra_cpu):
    """
    Ejecuta el flujo principal del juego del Gato.
    Alterna entre los jugadores y verifica al ganador.

    Args:
    es_contra_cpu : True si se juega contra la CPU, False si es jugador vs jugador.
    """
    # Inicializa el tablero
    tablero = crear_tablero_gato()
    # Define los símbolos para los jugadores
    jugadores = ['X', 'O']
    turno = 0  # Controla el turno actual
    jugando = True  # Indica si el juego continúa

    print("¡Bienvenido al juego del Gato!")

    while jugando:
        # Muestra el estado actual del tablero
        mostrar_tablero_gato(tablero)
        # Determina el jugador actual
        jugador_actual = jugadores[turno % 2]

        if jugador_actual == 'X' or not es_contra_cpu:
            # Turno del jugador humano
            print(f"Turno de {jugador_actual}.")
            # Solicita fila y columna al jugador
            fila = int(input("Elige una fila (1-3): ")) - 1  # Convierte a índice
            columna = int(input("Elige una columna (1-3): ")) - 1  # Convierte a índice
        else:
            # Turno de la CPU
            print(f"Es el turno de la CPU ({jugador_actual}).")
            fila, columna = cpu_jugar_gato(tablero)

        # Verifica si el movimiento es válido
        if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == ' ':
            # Realiza el movimiento
            tablero[fila][columna] = jugador_actual
            # Verifica si el jugador actual ha ganado
            if verificar_victoria_gato(tablero, jugador_actual):
                mostrar_tablero_gato(tablero)  # Muestra el tablero final
                print(f"¡{jugador_actual} ha ganado!")
                jugando = False  # Termina el bucle del juego
            else:
                turno += 1  # Cambia al siguiente turno
        else:
            # Movimiento inválido
            print("Movimiento inválido, intenta nuevamente.")


if __name__ == '__main__':
    # Pregunta si se desea jugar contra la CPU
    es_contra_cpu = input("¿Quieres jugar contra la CPU? (si/no): ").strip().lower() == 'si'
    # Inicia el juego
    jugar_gato(es_contra_cpu)
