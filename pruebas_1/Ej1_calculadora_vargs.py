def mostrar_menu() -> int:
    """
    Muestra un menú con opciones al usuario y solicita una opción.

    Returns:
    int: La opción seleccionada por el usuario.
    """
    print("**Menú**")
    print("[1].- Sumar")
    print("[3].- Multiplicar")
    print("[0].- Salir")
    opcion_usuario = int(input("Ingrese una opción: "))
    return opcion_usuario


def convertir_a_flotante(cadena: str) -> float | None:
    """
    Convierte una cadena a un número flotante si es válida.

    Args:
    cadena: Cadena introducida por el usuario.

    Returns:
    float: Número flotante si la cadena es válida.
    None: Si la cadena no puede convertirse.
    """
    sin_guiones = cadena.count("-")
    sin_puntos = cadena.count(".")
    revisar_cadena = cadena.lstrip("-").replace(".", "")
    if revisar_cadena.isnumeric() and sin_guiones in (0, 1) and sin_puntos in (0, 1):
        return float(cadena)
    else:
        return None


def realizar_suma(numero1: float, numero2: float) -> float:
    """
    Realiza la suma de dos números.

    Args:
    numero1 : Primer número a sumar.
    numero2 : Segundo número a sumar.

    Returns:
    float: Resultado de la suma.
    """
    resultado_suma = numero1 + numero2
    return resultado_suma


def realizar_multiplicacion(numero1: float, numero2: float) -> float:
    """
    Realiza la multiplicación de dos números.

    Args:
    numero1 : Primer número a multiplicar.
    numero2 : Segundo número a multiplicar.

    Returns:
    float: Resultado de la multiplicación.
    """
    resultado_multiplicacion = numero1 * numero2
    return resultado_multiplicacion


def ejecutar_programa() -> None:
    """
    Ejecuta el programa principal, mostrando el menú y realizando las operaciones seleccionadas.
    """
    opcion_usuario = None
    while opcion_usuario != 0:
        # Mostrar el menú y obtener la opción seleccionada
        opcion_usuario = mostrar_menu()
        if opcion_usuario == 0:
            # Salida del programa
            print("Saliendo del programa.")
        elif opcion_usuario == 1:
            # Realizar suma
            primer_numero: str = input("Ingrese un número: ")
            segundo_numero: str = input("Ingrese un segundo número: ")
            num1 = convertir_a_flotante(primer_numero)
            num2 = convertir_a_flotante(segundo_numero)

            # Validación de entradas
            while num1 is None or num2 is None:
                print("Opción no válida, intente de nuevo.")
                primer_numero: str = input("Ingrese un número: ")
                segundo_numero: str = input("Ingrese un segundo número: ")
                num1 = convertir_a_flotante(primer_numero)
                num2 = convertir_a_flotante(segundo_numero)

            # Mostrar el resultado de la suma
            resultado = realizar_suma(num1, num2)
            print(f"La suma es {resultado:.2f}")
        elif opcion_usuario == 3:
            # Realizar multiplicación
            primer_numero: str = input("Ingrese un número: ")
            segundo_numero: str = input("Ingrese un segundo número: ")
            num1 = convertir_a_flotante(primer_numero)
            num2 = convertir_a_flotante(segundo_numero)

            # Validación de entradas
            while num1 is None or num2 is None:
                print("Opción no válida, intente de nuevo.")
                primer_numero: str = input("Ingrese un número: ")
                segundo_numero: str = input("Ingrese un segundo número: ")
                num1 = convertir_a_flotante(primer_numero)
                num2 = convertir_a_flotante(segundo_numero)

            # Mostrar el resultado de la multiplicación
            resultado = realizar_multiplicacion(num1, num2)
            print(f"La multiplicación es {resultado:.2f}")
        else:
            # Opción no válida
            print("Opción incorrecta.")


if __name__ == '__main__':
    ejecutar_programa()
