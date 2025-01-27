import random  # Módulo random no se utiliza, podría eliminarse


def mostrar_tablero_4enraya(tablero):
    """
    Muestra el tablero de 4 en raya de forma simple.
    Cada fila del tablero se imprime con separadores para las columnas.
    """
    # Recorre cada fila del tablero y la imprime
    for fila in tablero:
        # Imprime la fila con separadores entre las celdas
        print(fila[0], "|", fila[1], "|", fila[2], "|", fila[3], "|", fila[4], "|", fila[5], "|", fila[6])
        # Imprime una línea divisoria entre filas
        print("-------------" * 2)


def es_columna_valida(tablero, columna):
    """
    Verifica si la columna seleccionada tiene espacio para colocar una ficha.

    Args:
    tablero: Matriz que representa el tablero de juego.
    columna: Índice de la columna a verificar.

    Returns:
    bool: True si la columna tiene espacio, False de lo contrario.
    """
    hay_lugar = True  # Representa que hay espacio en la columna
    no_hay_lugar = False  # Representa que no hay espacio en la columna
    # Verifica si la parte superior de la columna está vacía
    if tablero[0][columna] == " ":
        return hay_lugar
    return no_hay_lugar


def realizar_movimiento(tablero, columna, jugador):
    """
    Coloca una ficha en la columna seleccionada por el jugador.

    Args:
    tablero: Matriz que representa el tablero de juego.
    columna: Índice de la columna donde se colocará la ficha.
    jugador: Símbolo del jugador ('X' o 'O').

    Returns:
    bool: True si el movimiento fue exitoso, False si no hay espacio.
    """
    # Recorre las filas de abajo hacia arriba
    for fila in range(5, -1, -1):
        # Si encuentra una posición vacía, coloca la ficha
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            return True
    # Retorna False si no hay espacio en la columna
    return False


def verificar_victoria_4enraya(tablero, jugador):
    """
    Verifica si un jugador ha ganado el juego con 4 fichas consecutivas.
    Busca líneas horizontales, verticales y diagonales.

    Args:
    tablero : Matriz que representa el tablero de juego.
    jugador : Símbolo del jugador ('X' o 'O').

    Returns:
    bool: True si el jugador gana, False en caso contrario.
    """
    # Verificación horizontal
    for fila in tablero:
        for col in range(4):  # Solo evalúa hasta la columna 3
            if (fila[col] == jugador and fila[col + 1] == jugador and
                    fila[col + 2] == jugador and fila[col + 3] == jugador):
                return True

    # Verificación vertical
    for col in range(7):  # Recorre las columnas
        for fila in range(3):  # Solo evalúa hasta la fila 2
            if (tablero[fila][col] == jugador and tablero[fila + 1][col] == jugador and
                    tablero[fila + 2][col] == jugador and tablero[fila + 3][col] == jugador):
                return True

    # Verificación diagonal (izquierda a derecha)
    for fila in range(3):  # Solo evalúa las filas superiores
        for col in range(4):  # Evalúa las columnas con espacio para diagonales
            if (tablero[fila][col] == jugador and tablero[fila + 1][col + 1] == jugador and
                    tablero[fila + 2][col + 2] == jugador and tablero[fila + 3][col + 3] == jugador):
                return True

    # Verificación diagonal (derecha a izquierda)
    for fila in range(3):  # Solo evalúa las filas superiores
        for col in range(3, 7):  # Evalúa las columnas desde la 3 a la 6
            if (tablero[fila][col] == jugador and tablero[fila + 1][col - 1] == jugador and
                    tablero[fila + 2][col - 2] == jugador and tablero[fila + 3][col - 3] == jugador):
                return True

    # Si no hay victoria, retorna False
    return False


def jugar():
    """
    Ejecuta el flujo principal del juego 4 en raya.
    Maneja el tablero, alterna entre jugadores y verifica el ganador.
    """
    # Inicializa el tablero vacío
    tablero = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    jugador_actual = 'X'  # El jugador 'X' comienza
    no_hay_ganador = True  # Controla el bucle del juego

    while no_hay_ganador:
        # Muestra el tablero en su estado actual
        mostrar_tablero_4enraya(tablero)

        # Solicita la columna al jugador actual
        columna = int(input(f"Jugador {jugador_actual}, elige una columna (0-6): "))

        # Verifica si la columna es válida
        if columna < 0 or columna > 6:
            print("Columna inválida. Elige un número entre 0 y 6.")
            continue
        if not es_columna_valida(tablero, columna):
            print("Esa columna está llena. Elige otra.")
            continue

        # Realiza el movimiento del jugador
        realizar_movimiento(tablero, columna, jugador_actual)

        # Verifica si el jugador actual ha ganado
        if verificar_victoria_4enraya(tablero, jugador_actual):
            mostrar_tablero_4enraya(tablero)  # Muestra el tablero final
            print(f"¡Felicidades! El jugador {jugador_actual} ha ganado.")
            break

        # Cambia al otro jugador.
        jugador_actual = 'O' if jugador_actual == 'X' else 'X'


if __name__ == '__main__':
    jugar()
