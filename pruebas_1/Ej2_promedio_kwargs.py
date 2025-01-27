# Diccionario inicial del estudiante con calificaciones en 0.
estudiante = {
    'nombre': "Tania",
    'Electronica': 0,
    'Algebra': 0,
    'Estructura de datos': 0,
    'Derecho y legislacion': 0,
    'Contabilidad': 0,
    'Ingles': 0
}


def mostrar_menu() -> int:
    """
    Muestra el menú principal y solicita al usuario una opción.

    Returns:
     opción seleccionada por el usuario.
    """
    print("Promedio de un estudiante")
    print("1) Calcular promedio de un estudiante")
    print("0) Salir")
    opcion = input("Teclea la opción que desea realizar: ")

    # Validación de que la opción es numérica
    while not opcion.isnumeric():
        print("Opción no válida")
        opcion = input("Ingresa número nuevamente: ")

    return int(opcion)


def convertir_a_flotante(cadena):
    """
    Convierte una cadena a un número flotante si es válida.

    Args:
    cadena : Entrada proporcionada por el usuario.

    Returns:
    Número flotante si la cadena es válida, None en caso contrario.
    """
    sin_puntos = cadena.count(".")
    sin_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".", "")

    if revisar_cadena.isnumeric() and sin_puntos in (0, 1) and sin_guiones in (0, 1):
        return float(cadena)
    return None


def ingresar_estudiante(estudiante):
    """
    Solicita al usuario que ingrese el nombre y las calificaciones del estudiante.

    Args:
    estudiante : Diccionario donde se almacenan los datos del estudiante.
    """
    # Solicitar nombre del estudiante
    nombre_estudiante = input("Ingrese nombre del estudiante: ")
    while nombre_estudiante.isnumeric():
        print("Opción no válida")
        nombre_estudiante = input("Ingrese nuevamente el nombre del estudiante: ")
    estudiante['nombre'] = nombre_estudiante

    # Lista de materias para iterar
    materias = [
        "Electronica",
        "Algebra",
        "Estructura de datos",
        "Derecho y legislacion",
        "Contabilidad",
        "Ingles"
    ]

    # Solicitar calificaciones para cada materia
    for materia in materias:
        calificacion = input(f"Ingrese calificación de la materia de {materia}: ")
        numero = convertir_a_flotante(calificacion)

        while numero is None:
            calificacion = input(f"Acción inválida, ingrese nuevamente la calificación de {materia}: ")
            numero = convertir_a_flotante(calificacion)

        estudiante[materia] = numero


def calcular_promedio(estudiante):
    """
    Calcula el promedio de las calificaciones del estudiante.

    Args:
    estudiante (dict): Diccionario que contiene las calificaciones del estudiante.

    Returns:
    float: Promedio de las calificaciones.
    """
    total_calificaciones = 0
    # Materias que tienen calificaciones
    materias = ['Electronica', 'Algebra', 'Estructura de datos', 'Derecho y legislacion', 'Contabilidad', 'Ingles']

    # Sumar todas las calificaciones
    for materia in materias:
        total_calificaciones += estudiante[materia]

    # Calcular y retornar el promedio
    return total_calificaciones / len(materias)


if __name__ == '__main__':
    # Variable para controlar la ejecución del programa
    opcion = 1

    while opcion != 0:
        # Mostrar menú y obtener opción del usuario
        seleccion = mostrar_menu()

        if seleccion == 1:
            # Procesar información del estudiante
            ingresar_estudiante(estudiante)
            print("\nInformación del estudiante:")
            print(estudiante)

            # Calcular y mostrar el promedio
            promedio = calcular_promedio(estudiante)
            print(f"Promedio final del estudiante: {promedio:.2f}")

        elif seleccion == 0:
            # Salir del programa
            print("Salió del programa")
            break

        else:
            # Opción no válida
            print("Opción incorrecta")
