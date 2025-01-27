# main.py
from juegos import ahorcado, gato, raya4

def main():
    print("¡Bienvenido al Menú de Juegos!")
    opcion = ""

    while opcion != "4":
        print("\nSelecciona una opción:")
        print("1. Juego del Ahorcado")
        print("2. Juego del Gato")
        print("3. Juego de 4 en Raya")
        print("4. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            ahorcado()
        elif opcion == "2":
            gato()
        elif opcion == "3":
            raya4()
        elif opcion == "4":
            print("Gracias por jugar. ¡Hasta la próxima!")
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
