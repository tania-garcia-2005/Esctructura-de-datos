from random import randint# .....................

print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓Fecha: 24 de Noviembre de 2024     🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print()
print("----------------------------------------------------------------------------------")
#constantes para las opciones del juego.
PIEDRA = "Piedra"
PAPEL = "Papel"
TIJERAS = "Tijeras"


# Función para mostrar mi menú y pedir la opción al usuario.
def mostrar_menu():
    print()
    print("-----------------------------------------------------------------")
    print("****** ★彡『 JUEGO DE PIEDRSA PAPEL O TIJERAS 』彡★ ******")
    print("-----------------------------------------------------------------")
    print()

    print(f"Victorias del jugador: {victorias_jugador}, Empates: {empates}, Victorias del CPU: {victorias_cpu}")
    print("1) Piedra.")
    print("2) Papel.")
    print("3) Tijeras.")
    print("0) Salir.")
    print()
    opcion = int(input("Ingresa una opción: "))
    return opcion


# variables de conteo
victorias_jugador = 0
empates = 0
victorias_cpu = 0

#las utilice para las  elecciones
jugador = ""
cpu = ""


opcion_jugador = None
while opcion_jugador != 0:
    # Muestra mi menú y obtiene  la opción ingresada por el usuario.
    opcion_jugador = mostrar_menu()

    if opcion_jugador == 0:
        print("Fin del juego. ¡Gracias por jugar!")
        opcion_jugador = 0  #termina el bucle con el cero.
    else:
        # La CPU elige aleatoriamente su eleccion .
        opcion_cpu = randint(1, 3)

        # elecciones de jugador y CPU.
        if opcion_jugador == 1:
            jugador = PIEDRA
        elif opcion_jugador == 2:
            jugador = PAPEL
        elif opcion_jugador == 3:
            jugador = TIJERAS

        if opcion_cpu == 1:
            cpu = PIEDRA
        elif opcion_cpu == 2:
            cpu = PAPEL
        elif opcion_cpu == 3:
            cpu = TIJERAS

        #  determinar el ganador
        if jugador == cpu:
            empates += 1
            resultado = f"Empate. Jugador: {jugador}, CPU: {cpu}"
        elif (jugador == PIEDRA and cpu == TIJERAS) or (jugador == PAPEL and cpu == PIEDRA) or (
                jugador == TIJERAS and cpu == PAPEL):
            victorias_jugador += 1
            resultado = f"El ganador es el Jugador. Jugador: {jugador}, CPU: {cpu}"
        else:
            victorias_cpu += 1
            resultado = f"El ganador es el CPU. Jugador: {jugador}, CPU: {cpu}"

        # Mostrar el resultado .
        print(resultado)
        print("-" * 30)
#si elige la opcio 0,sale del programa improimiendo el mensaje:
print("Fin del juego. ¡Gracias por jugar!,has salido exitosamente del programa")
