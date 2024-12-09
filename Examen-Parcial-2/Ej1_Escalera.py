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
    #Solicita al usuario el número de escalones.
    # Este número puede ser positivo (ascendente), negativo (descendente), o cero (para salir).
    numero = int(input("Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir: "))
    print()  #Espacio.
    return numero

#Título del programa
print(" *  🌸ꗥ～ꗥ🌸 EJERCICIO 1_LA ESCALERA 🌸ꗥ～ꗥ🌸 * ")
print()

# Inicializa la variable para el ciclo(-1).
eleccion = None

#Hasta que el usuario ingrese 0 sale.
while eleccion != 0:
#Guarda el número de escalones que el usuario ingreso,al momento en el que se le solicito.
    eleccion = obtener_escalones()

    #Verifica si el usuario ingresó el número cero o no.
    if eleccion == 0:
        #Muestra el mensaje de despedida y sale del ciclo.
        print("Usted ha salido exitosamente del programa,gracias por usar el programa, hasta luego!")
        break
    #Aquí verifica  si el número ingresado es positivo
    elif eleccion > 0:
        #En este apartado hace la escalera ascendente(hacia arriba).
        for paso in range(1, eleccion + 1):  # Empieza desde 1 hasta el número de escalones ingresados.
            # Aquí se calcula la cantidad de espacios necesarios para alinear el escalón.
            print(" " * (eleccion - paso) * 2 + "_|")  # Imprimir el escalón con espacios y símbolo
    # Verifico si el número ingresado es negativo.
    elif eleccion < 0:
        # Genero la escalera descendente(Hacia abajo).
        print("_")  # Imprimo el primer escalón.
        for paso in range(1, -eleccion + 1):  #Empieza desde 1 hasta el valor absoluto(Si el número es positivo, el valor absoluto es el mismo número.
#Si el número es negativo, el valor absoluto es como quitarle el signo negativo del número ingresado.
            # Calcula la cantidad de espacios necesarios para alinear el escalón descendente(Hacia abajo).
            print(" " * (paso * 2) + "|_")  # Imprimí el escalón con los espacios y símbolo.
    else:
        # En caso de ingresar otra cosa aparese:
        print("Opción no válida, intente nuevamente.")


