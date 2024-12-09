'''
Descripción del programa:

Este programa dibuja una escalera, en donde el usuario ingresa el número de escalores.

Si el número es positivo, la escalera será ascendente. Un ejemplo cuando se ingresa un valor de 4:

        _
      _|
    _|
  _|
_|

Si el número es negativo, la escalera será descendente. Un ejemplo cuando se ingresa un valor de -4:

_
 |_
   |_
     |_
       |_

Si el número es cero, se deberá salir del programa.


Se debe mostrar la siguiente pantalla:

  ***  Ejercicio 1. La escalera.  ***

Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir:

Cualquier otro caso -> Opción no válida.

Para ello:

a) Solicite el número de escalones utilizando un ciclo.

b) Muestre la escalera utilizando la lógica adecuada. Se requiere utilizar funciones para dibujar las escaleras para considerar el ejercicio como completo.
'''
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

    # Aquí verifica si el número ingresado es positivo.
    elif eleccion > 0:
        # En este apartado hace la escalera ascendente (hacia arriba).
        for paso in range(1, eleccion + 1):  # Empieza desde 1 hasta el número de escalones ingresados.
            # Aquí se calcula la cantidad de espacios necesarios para alinear el escalón.
            print(" " * (eleccion - paso) * 2 + "_|")  # Imprimir el escalón con espacios y símbolo.

    # Verifico si el número ingresado es negativo.
    elif eleccion < 0:
        # Genero la escalera descendente (hacia abajo).
        for paso in range(-eleccion):  # Desde 0 hasta el valor absoluto del número negativo ingresado.
            # Aquí se calcula la cantidad de espacios necesarios para alinear el escalón descendente (hacia abajo).
            print(" " * (paso * 2) + "|_")  # Imprimí el escalón con los espacios y símbolo.
        print("_")  # Imprime la base de la escalera al final.

    else:
        # En caso de ingresar otra cosa aparece:
        print("Opción no válida, intente nuevamente.")


