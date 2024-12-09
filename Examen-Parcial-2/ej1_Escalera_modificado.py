print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓                                🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print()
print("----------------------------------------------------------------------------------")
print()


def obtener_escalones():
    # Solicita al usuario el número de escalones.
    # Este número puede ser positivo (ascendente), negativo (descendente), o cero (para salir).
    numero = int(input(
        "Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir: "))
    print()
    return numero


# Título de mi programa.
print(" *  🌸ꗥ～ꗥ🌸 EJERCICIO 1_LA ESCALERA 🌸ꗥ～ꗥ🌸 * ")
print()

# Inicializa la variable para el ciclo.
eleccion = None  # (-1).

# Hasta que el usuario ingrese 0 se sale del programa.
while eleccion != 0:
    # Guarda el número de escalones que el usuario ingresó al momento en el que se le solicitó.
    eleccion = obtener_escalones()

    # Verifica si el usuario ingresó el número cero o no.
    if eleccion == 0:
        # Muestra el mensaje de despedida.
        print("Usted ha salido exitosamente del programa, gracias por usar el programa, ¡hasta luego!")
        eleccion = 0  # Establece `elección` en 0 para salir del ciclo.

    # Aquí verifica si el número ingresado es negativo.##########
    elif eleccion < 0:
        # Genero la escalera descendente (hacia abajo).
        for paso in range(-eleccion + 1):  # Desde 0 hasta el valor absoluto del número negativo ingresado(aquí lo modifízque para que añada un escalón más).
            # Aquí se calcula la cantidad de espacios necesarios para alinear el escalón descendente (hacia abajo).
            print(" " * (-eleccion + 1 - paso) * 2 + "_|")
              # Imprimí el escalón con los espacios y símbolo.
        print("_")  # Imprime la base de la escalera al final.
    # Verifico si el número ingresado es negativo.##
    elif eleccion > 0:
        # En este apartado hace la escalera ascendente (hacia arriba).
        for paso in range(eleccion + 1):  # Empieza desde 1 hasta el número de escalones ingresados, pero le suma uno a la elección.
            # Aquí se calcula la cantidad de espacios necesarios para alinear el escalón(a la elecccion le sume un 1)de este modo ya los alinea bien.
            print(" " * (paso * 2) + "|_")  # Imprimir el escalón con espacios y símbolo.
    else:
        # En caso de ingresar otra cosa aparece:
        print("Opción no válida, intente nuevamente.")

