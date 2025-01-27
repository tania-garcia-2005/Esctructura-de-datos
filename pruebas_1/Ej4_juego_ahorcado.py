import random

def jugar_ahorcado():
    """
    Ejecuta el juego del Ahorcado.
    El jugador debe adivinar una palabra relacionada con un tema (frutas, verduras o animales)
    antes de que se acaben los intentos disponibles.

    Args:
    No recibe argumentos.

    Returns:
    No retorna valores, solo imprime el estado del juego en cada paso.
    """
    # Diccionario que contiene las palabras organizadas por temas
    palabras = {
        "frutas": ["manzana", "sandia", "melon", "fresa"],
        "verduras": ["chile", "tomate", "zanahoria"],
        "animales": ["gato", "perro", "delfin", "chivo"]
    }

    # Elegir un tema aleatorio
    tema = random.choice(list(palabras.keys()))  # Selección aleatoria del tema
    palabra_secreta = random.choice(palabras[tema])  # Selección aleatoria de la palabra dentro del tema

    letras_adivinadas = []  # Lista para guardar las letras que el usuario ha adivinado
    intentos = 6  # Número máximo de intentos permitidos

    print(f"Bienvenido al juego del Ahorcado! El tema es: {tema}")

    while intentos > 0:
        # Construcción de la palabra oculta según las letras adivinadas
        palabra_oculta = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_oculta += letra
            else:
                palabra_oculta += "_"

        print(f"Palabra: {palabra_oculta}")
        print(f"Intentos restantes: {intentos}")

        # Solicitar al usuario que ingrese una letra
        letra = input("Adivina una letra: ")

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta otra vez.")
        elif letra in palabra_secreta:
            letras_adivinadas.append(letra)  # Se agrega la letra a la lista de adivinadas
            print("\u00a1Bien hecho! Has adivinado una letra.")
        else:
            letras_adivinadas.append(letra)
            intentos = intentos - 1  # Se reduce el número de intentos disponibles
            print(f"\u00a1Letra incorrecta! Quedan {intentos} intentos.")

        # Verificar si el usuario ha adivinado toda la palabra
        palabra_completa = True
        for letra in palabra_secreta:
            if letra not in letras_adivinadas:
                palabra_completa = False
                break

        if palabra_completa:
            print(f"\u00a1Felicidades! Has adivinado la palabra: {palabra_secreta}")
            break

    if intentos == 0:
        print(f"Has perdido. La palabra era: {palabra_secreta}")

if __name__ == '__main__':
    jugar_ahorcado()
