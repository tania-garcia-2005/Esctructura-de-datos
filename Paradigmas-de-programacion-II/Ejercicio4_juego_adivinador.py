#***************************************
#****   Tania Garcia Flores.      ******
#****   31 de octubre de 2024.    ******
#***************************************

print()
print("******juego del adivinador******")
print()

from random import randint

intentos_maximos = 5
intentos = 0
numero_secreto = randint(1, 100)
print("¡Bienvenido al juego de adivinar el número!")
print("He elegido un número entre 1 y 100. Tienes 5 intentos para adivinarlo.")

while intentos < intentos_maximos:
    intento_usuario = input("Ingresa tu numero que tu supones que es: ")

    intento_usuario = int(intento_usuario)  # esto hace que se conviertan las entradas pero en numeros
    intentos += 1  # en este punto aumenta los intentos

    # aqui verifica si la entrada es correcta
    if intento_usuario < numero_secreto:
        print("El número es mayor. puedes intentarlo de nuevo.")
    elif intento_usuario > numero_secreto:
        print("El número es menor. puedes intentarlo de nuevo.")
    else:
        print(f" wow ¡Felicidades! Adivinaste el número,muy bien {numero_secreto} en {intentos} intentos.")
        break#en caso de que adivine el número el juego termina y para eso ocupe el break.
else:
    print(f"losiento no  lograste adivinar el número. pero el  número secreto era: {numero_secreto}.")
