# Mi portada
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓                                🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print()
print("----------------------------------------------------------------------------------")
print()


# Función para mi menú.
def mostrar_menu():
    print("*** Test del sombrero seleccionador de Harry Potter. ***")
    print("Este programa determina a qué casa perteneces según tus respuestas.")
    print("\n1) Comenzar el test.")
    print("0) Salir.")
    opcion = int(input("Elige una opción: "))  # Opción del usuario.
    print("---------------------------------------------------")
    return opcion


# Función para hacer las preguntas del test y contar las respuestas
def hacer_test():
    # Lista de preguntas con sus opciones y las casas que corresponde.
    preguntas = [

        ("¿Qué preferirías que la gente no dijera de ti?",
         ["Ordinario (blabla)", "Ignorante ", "Cobarde ", "Egoísta"]),
        # Si pongo en paréntesis las casas aparecen en la pantalla; si no, no.
        ("¿Qué te gustaría que hicieran al recordar tu nombre?",
         ["Te extrañen", "Cuenten tus historias", "Admiren tus logros ", "No me importa"]),
        ("¿Qué poción te gustaría inventar?",
         ["Gloria ", "Poder", "Amor", "Sabiduría "]),
        ("¿Cómo te describirías en una palabra?",
         ["Valiente", "Ambicioso ", "Leal", "Curioso"]),
        ("¿Qué cualidad te representa mejor?",
         ["Fuerza ", "Astucia ", "Paciencia", "Inteligencia "]),
        ("¿Qué super poder preferirías tener?",
         ["Invisibilidad", "Dormir ", "Super fuerza ", "Teletransportarse"])

    ]

    # Puntos para cada casa que los inicializo en 0.
    puntos_griffindor = 0
    puntos_slytherin = 0
    puntos_hufflepuff = 0
    puntos_ravenclaw = 0

    # Hace cada pregunta.
    for pregunta, opciones in preguntas:
        print(pregunta)  # Muestra la pregunta
        print("1)", opciones[0])  # Muestra la opción 1
        print("2)", opciones[1])  # Muestra la opción 2
        print("3)", opciones[2])  # Muestra la opción 3
        print("4)", opciones[3])  # Muestra la opción 4
        seleccion = int(input("Elige una opción: "))  # Aquí el usuario elige una opción y se guarda en(seleccion).

        # Sumo los puntos a la casa correspondiente de la respuesta que elija el usuario.
        if seleccion == 1:
            puntos_griffindor += 1
        elif seleccion == 2:
            puntos_slytherin += 1
        elif seleccion == 3:
            puntos_hufflepuff += 1
        elif seleccion == 4:
            puntos_ravenclaw += 1

        print("---------------------------------------------------")

    # Calculo la casa ganadora.
    if puntos_griffindor > puntos_slytherin and puntos_griffindor > puntos_hufflepuff and puntos_griffindor > puntos_ravenclaw:
        casa = "Gryffindor"  # Si Gryffindor tiene más puntos, es la casa elegida.
    elif puntos_slytherin > puntos_griffindor and puntos_slytherin > puntos_hufflepuff and puntos_slytherin > puntos_ravenclaw:
        casa = "Slytherin"  # Si Slytherin tiene más puntos, es la casa elegida.
    elif puntos_hufflepuff > puntos_griffindor and puntos_hufflepuff > puntos_slytherin and puntos_hufflepuff > puntos_ravenclaw:
        casa = "Hufflepuff"  # Si Hufflepuff tiene más puntos, es la casa elegida.
    else:
        casa = "Ravenclaw"  # Si Ravenclaw tiene más puntos, es la casa elegida.

    # Mi resultado final.
    print("¡Felicidades! El sombrero seleccionador te ha asignado a la casa de:", casa)
    print("---------------------------------------------------")


# Ejecuta el test.
opcion = None  # (-1)#Variable para almacenar la opción seleccionada.
while opcion != 0:  # Para hasta que el usuario seleccione la opción 0 (salir).
    opcion = mostrar_menu()  # Llama a la función que muestra el menú y obtiene la opción que ingreso el usuario.

    if opcion == 1:  # Si la opción es 1, inicia el test.
        hacer_test()  # Llama a la función que realiza el test.
    elif opcion == 0:  # Si la opción es 0,Fin de mi programa.
        print("Usted ha salido exitosamente del programa.Gracias por usar este programa y hacer el Test.")
        print("---------------------------------------------------")
    else:  # Por si la opción no es valida.
        print("Opción no válida.Por favor ingrese una opción entre 0 y 1.")
        print("---------------------------------------------------")
