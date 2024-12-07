# Esta función se usa para generar números aleatorios.
from random import randint

# Mi portada.
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓Fecha: 24 de Noviembre de 2024     🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print()
print("----------------------------------------------------------------------------------")

# Definición de mis variables para las opciones.
PIEDRA = "Piedra"
PAPEL = "Papel"
TIJERAS = "Tijeras"

#Defrinición de mi menú.
def mostrar_menu():
    print()
    print("-----------------------------------------------------------------")
    print("****** ★彡『 JUEGO DE PIEDRA PAPEL O TIJERAS 』彡★ ******")
    print("-----------------------------------------------------------------")
    print()

# Muestro las: victorias, empates y derrotas de mi juego.
    print(f"Victorias del jugador: {victorias_jugador}, Empates: {empates}, Victorias del CPU: {victorias_cpu}")
    print("1) Piedra.")
    print("2) Papel.")
    print("3) Tijeras.")
    print("0) Salir.")
    print()

#Solicito que el usuario ingrese una opción y la devuelve como número entero.
    opcion = int(input("Ingresa una opción: "))
    return opcion

# Definición de mis variables las cuales llevarán el conteo de victorias, empates y derrotas de mi juego.
victorias_jugador = 0#se inicializan en cero y van sumandose según sea el caso.
empates = 0
victorias_cpu = 0

#En estas variables se van a almacenar las elecciones del usuario(jugador) y de la cpu.
jugador = ""
cpu = ""

#Se repite mientras que el usuario no elija la opción cero la cúal hace que salga del juego.
opcion_jugador = None#Es como si hubiese un -1.
while opcion_jugador != 0:
    # Llamada a mi función menú para mostrar el menú y obtiene la opción que seleccionó el usuario.
    opcion_jugador = mostrar_menu()

    # Si el usuario elige la opción cero, termina el juego.
    if opcion_jugador == 0:
        print("Usted ha salido exitosamente del juegos. ¡Gracias por jugar mi juego!")
        opcion_jugador = 0
    else:
        #La cpu elige una opción aleatoria entre:piedra, papel y tijera.
        opcion_cpu = randint(1, 3)# de 1 a 3.

        #Elección del usuario.
        if opcion_jugador == 1:
            jugador = PIEDRA
        elif opcion_jugador == 2:
            jugador = PAPEL
        elif opcion_jugador == 3:
            jugador = TIJERAS

        #Opción de la cpu.
        if opcion_cpu == 1:
            cpu = PIEDRA
        elif opcion_cpu == 2:
            cpu = PAPEL
        elif opcion_cpu == 3:
            cpu = TIJERAS

        #Aquí determino los resultados del juego usando las compuertas lógicas and y or.
        if jugador == cpu:
            empates += 1  # Si  son iguales, es empate.
            resultado = f"Empate. Jugador: {jugador}, CPU: {cpu}"
        elif (jugador == PIEDRA and cpu == TIJERAS) or (jugador == PAPEL and cpu == PIEDRA) or (jugador == TIJERAS and cpu == PAPEL):
            victorias_jugador += 1
            resultado = f"El ganador es el Jugador. Jugador: {jugador}, CPU: {cpu}"
        else:
            victorias_cpu += 1  # La cpu gana en cualquier otro caso.
            resultado = f"El ganador es el CPU. Jugador: {jugador}, CPU: {cpu}"

        # Muestra el resultado de la ronda del juego y una línea.
        print(resultado)
        print("-" * 30)

