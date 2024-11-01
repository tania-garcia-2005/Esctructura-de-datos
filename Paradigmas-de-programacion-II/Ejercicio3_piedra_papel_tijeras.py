#***************************************
#****   Tania Garcia Flores.      ******
#****   31 de octubre de 2024.    ******
#***************************************


print()
print("******JUEGO DE PIEDRA PAPEL O TIJERA   ******")
print()


from random import randint

print("** JUEGO DE PIEDRA PAPEL O TIJERA **\n")


victorias_jugador = 0
empates = 0
victorias_cpu = 0
contador = 1  #mantiene contolado el  ciclo

while contador != 0:
    opcion_cpu = randint(1, 3)  # 1: Piedra, 2: Papel, 3: Tijera

    print("\nElige una opción:")
    print("1) Piedra")
    print("2) Papel")
    print("3) Tijera")
    print("0) Salir")

    opcion_usuario = int(input("Ingresa una opción: "))

    if opcion_usuario == 0:
        contador = 0  # Cambia el valor para salir del ciclo
    elif opcion_usuario == 1:
        eleccion_usuario = "Piedra"
    elif opcion_usuario == 2:
        eleccion_usuario = "Papel"
    elif opcion_usuario == 3:
        eleccion_usuario = "Tijera"
    else:
        print("La pción no es válida, por favor intenta de nuevo.")
        contador = contador  #  evita que el ciclo termine asi nadamas.


    if contador == 0:
        break  # termina y sale del ciclo cuando el jugador elige salir

    # esto es lo que elije  la CPU.
    if opcion_cpu == 1:
        eleccion_cpu = "Piedra"
    elif opcion_cpu == 2:
        eleccion_cpu = "Papel"
    elif opcion_cpu == 3:
        eleccion_cpu = "Tijera"

    # Muestra las elecciones en una sola oración
    print(f"Elegiste: {eleccion_usuario} | La CPU eligió: {eleccion_cpu}")

    # resultados finales
    if opcion_usuario == opcion_cpu:
        empates += 1
        print("Resultado: Empate")
    elif (opcion_usuario == 1 and opcion_cpu == 3) or (opcion_usuario == 2 and opcion_cpu == 1) or (opcion_usuario == 3 and opcion_cpu == 2):
        victorias_jugador += 1
        print("Resultado: Ganaste")
    else:
        victorias_cpu += 1
        print("Resultado: Ganó la CPU")

# datos finales.
print("\nGracias por jugar!")
print(f"Victorias del Jugador: {victorias_jugador}")
print(f"Empates: {empates}")
print(f"Victorias de la CPU: {victorias_cpu}")