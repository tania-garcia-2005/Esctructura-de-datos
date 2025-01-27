"""
Descripción:
En este archivo se ejemplifica cómo se deben especificar los tipos de datos de los parámetros y
de retorno en las funciones.
Especificar los tipos de datos y de retorno es fundamental para escribir código limpio, eficiente y mantenible.
"""


""" %%%%%%%     FUNCIONES    %%%%%%%%%%%%%%%%%%%%% """
# En esta función, se está especificando que la función regresa un valor de tipo entero.
def menu() -> int:
    print("  ***  Conversión a números enteros y flotantes con verificación ***")
    print("     1) Convertir a entero.")
    print("     2) Convertir a flotante.")
    print("     0) Salir.")
    print()

    opcion = input("Ingresa una de las opciones: ").strip()

    # Se verifica que la cadena ingresada sea un número.
    while not opcion.isnumeric():
        opcion = input("Opción no válida, intenta nuevamente: ")

    print()

    return int(opcion)


# En esta función, el argumento que recibe es de tipo cadena, y se regresa un tipo entero o None.
def cadena_a_entero(cadena: str) -> int | None:
    no_guiones = cadena.count("-")
    revisar_cadena =cadena.lstrip('-')

    if revisar_cadena.isnumeric() and no_guiones in (0, 1):
        return int(cadena)
    else:
        return None


# En esta función, el argumento que recibe es de tipo cadena, y se regresa un tipo flotante o None.
def cadena_a_flotante(cadena: str) -> float | None:
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena =cadena.lstrip('-').replace(".","")

    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
# Ciclo que contiene el menú.
opcion = None

while opcion != 0:

    opcion = menu()

    # Se escoge convertir a un número entero.
    if opcion == 1:
        num_cadena = input("Ingresa el número a convertir: ")
        numero = cadena_a_entero(num_cadena)

        while numero is None:
            num_cadena = input("Formato no válido, intenta nuevamente: ")
            numero = cadena_a_entero(num_cadena)

        print()
        print(f"El número {numero} es de tipo {type(numero)}.")

    # Se escoge convertir a un número flotante.
    elif opcion == 2:
        num_cadena = input("Ingresa el número a convertir: ")
        numero = (cadena_a_flotante(num_cadena))

        while numero is None:
            num_cadena = input("Formato no válido, intenta nuevamente: ")
            numero = cadena_a_flotante(num_cadena)

        print()
        print(f"El número {numero} es de tipo {type(numero)}.")

    # Se escoge salir del programa.
    elif opcion == 0:
        print("Fin del programa.")

    # Se escoge una opción no válida.
    else:
        print("Opción no válida.")

    print("------------------------------------------------------------------")
    print()
