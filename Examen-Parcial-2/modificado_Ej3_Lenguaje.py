#este programa se debe modificar para que haga,modifica los numeros por los digitos.


# Mi portada.
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓                                🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print()
print("----------------------------------------------------------------------------------")
print()

# Variable global para guardar resultados
resultado_conversion = {"resultado": ""}

# Esta función la uso para convertir el texto a un lenguaje básico.
def cambiar_a_basico(frase):
    # Mi diccionario para cambiar las vocales a lenguaje básico.
    cambio_vocales = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        'u': '(_)',
        'A': '4',
        'E': '3',
        'I': '1',
        'O': '0',
        '0':'o',
        '1': 'L',
        '2': 'R',
        '3': 'E',
        '4': 'A',
        '5': 'S',
        '6': 'b',
        '7': 'T',
        '8': 'B',
        '9': 'g',
        'U': '(_)'
    }
    resultado_conversion["resultado"] = ""  #El resultado anterior lo limpio.
    for letra in frase:
        resultado_conversion["resultado"] += cambio_vocales.get(letra, letra)

# Esta función me convierte el texto a un lenguaje intermedio.
def cambiar_a_intermedio(frase):
    cambio_intermedio = {
        'a': '4',
        'b': 'I3',
        'c': '[',
        'd': ')',
        'e': '3',
        'f': '|=',
        'g': '&',
        'h': '#',
        'i': '1',
        'j': ',_|',
        'k': '>|',
        'l': '1',
        'm': r'/\/\\',
        'n': r'|\|',
        'o': '0',
        'p': '|*',
        'q': '(_,)',
        'r': 'I2',
        's': '5',
        't': '7',
        'u': '(_)',
        'v': r'\/',
        'w': r'\/\/',
        'x': '><',
        'y': 'j',
        'z': '2',
        'A': '4',
        'B': 'I3',
        'C': '[',
        'D': ')',
        'E': '3',
        'F': '|=',
        'G': '&',
        'H': '#',
        'I': '1',
        'J': ',_|',
        'K': '>|',
        'L': '1',
        'M': r'/\/\\',
        'N': r'|\|',
        'O': '0',
        'P': '|*',
        'Q': '(_,)',
        'R': 'I2',
        'S': '5',
        'T': '7',
        'U': '(_)',
        'V': r'\/',
        'W': r'\/\/',
        'X': '><',
        'Y': 'j',
        'Z': '2'
    }
    resultado_conversion["resultado"] = ""  #El resultado anterior lo limpio.
    for letra in frase:
        resultado_conversion["resultado"] += cambio_intermedio.get(letra, letra)

# Función para mostrar mi menú.
def mostrar_menu():
    print("🌸ꗥ～ꗥ🌸 𝐄𝐣𝐞𝐫𝐜𝐢𝐜𝐢𝐨 𝟑. LENGUAJE HACKER (𝐥𝟑𝟑𝐭 𝐬𝐩𝟑𝟒𝐤) 🌸ꗥ～ꗥ🌸")
    print("1) Convertir texto a lenguaje básico.")
    print("2) Convertir texto a lenguaje intermedio.")
    print("0) Salir.")
    opcion = int(input("Ingrese una de las opciones: "))
    print("---------------------------------------------------")
    return opcion

opcion_seleccionada = None
while opcion_seleccionada != 0:
    opcion_seleccionada = mostrar_menu()

    if opcion_seleccionada == 1:  # Opción 1.
        texto = input("Introduce el texto para convertir a lenguaje básico: ")
        cambiar_a_basico(texto)
        print("Texto convertido:", resultado_conversion["resultado"])
        print("---------------------------------------------------")

    elif opcion_seleccionada == 2:  # Si elige la opción 2.
        texto = input("Introduce el texto para convertir a lenguaje intermedio: ")
        cambiar_a_intermedio(texto)
        print("Texto convertido:", resultado_conversion["resultado"])
        print("---------------------------------------------------")

    elif opcion_seleccionada == 0:  # Opción 0.
        print("Usted ha salido exitosamente del programa, ¡Gracias por usarlo!")
        print("---------------------------------------------------")

    else:  # Cuando elige una opción no válida.
        print("Opción no válida. Por favor, intente nuevamente ingresando un número entre 0 y 2.")
        print("---------------------------------------------------")


