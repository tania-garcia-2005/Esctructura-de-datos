'''
Descripción del programa:

Este programa convierte un texto al lenguaje hacker (lenguaje leet o 1337). Esta escritura se caracteriza por reemplazar las letras por números y símbolos.

Revisa la siguiente página para mayor información: https://www.gamehouse.com/blog/leet-speak-cheat-sheet/


Lenguaje básico:

En el lenguaje básico se sustituye cada vocal por un número.
La A se convierte en un 4, la E en un 3, la I en un 1 y la O en un cero.
La letra U es una excepción, ya que no hay un número obvio, por lo que se sustituye por (_).


Lenguaje intermedio:

En el lenguaje intermedio también se sustituyen las consonantes por números o signos de puntuación.
Por ejemplo, la B se convierte en I3, la C en [, la D en ), la L en 1.
Revisa la "Leet speak alphabet" de la página anterior y toma la primera de las opciones para el lenguaje.
Nota que no hay caracteres acentuados, por lo no se deben de convertir.


Se debe mostrar el siguiente menú:

  ***  Ejercicio 3. Lenguaje hacker (l33t sp34k).  ***

1) Convertir un texto a lenguaje básico.

2) Convertir un texto a lenguaje intermedio.

0) Salir.

Cualquier otro caso -> Opción no válida.

Para ello:

a) Utilice la lógica adecuada para mostrar las conversiones. No utilice funciones como bin() o hex().

a) Utilice la lógica adecuada para convertir el texto al lenguaje hacker básico o intermedio, según sea el caso.

b) Se debe convertir los caracteres sin importar si son mayúsculas o minúsculas, sin modificar los caracteres que no se convirtieron. Ejemplos con el lenguaje básico: hola -> h0l4, Hola -> H0l4, HOLA -> H0L4.

'''
# Mi portada.
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓                                🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print()
print("----------------------------------------------------------------------------------")
print()
#Esta función la uso para convertir el texto a un lenguaje básico.
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
        'U': '(_)'
    }
    #Estas variables me guardan el texto ya convertido.
    resultado = ""
    # Recorre cada letra y cambia si está en el diccionario.
    for letra in frase:
        resultado += cambio_vocales.get(letra, letra)  #Lo deja igual si no está en el diccionario.
    return resultado

# Esta función me convierte el texto a un lenguaje intermedio.
def cambiar_a_intermedio(frase):
    # Diccionario para cambiar letras a lenguaje intermedio.
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
        #Para mis mayúsculas.
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
    #Aquí mi variable guarda el texto convertido.
    resultado = ""
    # Recorre cada letra y cambia si está en el diccionario.
    for letra in frase:
        resultado += cambio_intermedio.get(letra, letra)  # Deja igual si no está en el diccionario.
    return resultado

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

    if opcion_seleccionada == 1:  #Opción 1.
        texto = input("Introduce el texto para convertir a  lenguaje básico: ")
        resultado = cambiar_a_basico(texto)
        print("Texto convertido:", resultado)
        print("---------------------------------------------------")

    elif opcion_seleccionada == 2:  # Si elige la opción 2.
        texto = input("Introduce el texto para convertir a lenguaje intermedio: ")
        resultado = cambiar_a_intermedio(texto)
        print("Texto convertido:", resultado)
        print("---------------------------------------------------")

    elif opcion_seleccionada == 0:  #Opción 0.
        print("Usted ha salido exitosamente del programa,Gracias por usarlo.")
        print("---------------------------------------------------")

    else:  #Cuando elige una opción no válida.
        print("Opción no válida.Po favor intente nuevamente ingresando un número entre 0 y 2.")
        print("---------------------------------------------------")
