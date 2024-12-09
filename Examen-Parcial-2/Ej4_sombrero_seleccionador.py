'''
Descripción del programa:

Este programa es un test de la elección del sombrero seleccionador de Harry Potter para alguna de las casas: Gryffindor, Slytherin, Hufflepuff y Ravenclaw.

Ejemplos de preguntas:

¿Cuál de las siguientes opciones odiarías más que la gente te llamara?
Gryffindor - Ordinario.
Slytherin - Ignorante.
Hufflepuff - Cobarde.
Ravenclaw - Egoísta.

Después de tu muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?
Gryffindor - Te extraña, pero sonríe.
Slytherin - Pide más historias sobre tus aventuras.
Hufflepuff - Piensa con admiración tus logros.
Ravenclaw - No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta.


Dada la opción, preferirías inventar una poción que garantizara:
Gryffindor - Gloria.
Slytherin - Sabiduría.
Hufflepuff - Amor.
Ravenclaw - Poder.


¿Cómo te definirías en una sola palabra?
Gryffindor - Valiente.
Slytherin - Ambicioso.
Hufflepuff - Leal.
Ravenclaw - Curioso.


¿Qué cualidad te describe mejor?
Gryffindor - La fuerza.
Slytherin - La astucia.
Hufflepuff - La paciencia.
Ravenclaw - La inteligencia.


¿Cuál es tu clase favorita?
Gryffindor - Vuelo.
Slytherin - Defensa contra las artes oscuras.
Hufflepuff - Animales fantásticos.
Ravenclaw - Pociones.


¿Cuál es tu lenguaje de programación favorito?
Gryffindor - C.
Slytherin - Python.
Hufflepuff - C++.
Ravenclaw - JavaScript.

Se debe mostrar la siguiente pantalla inicial:

  ***  Ejercicio 4. Test del sombrero seleccionador de Harry Potter.  ***

Este programa determina la casa (Gryffindor, Slytherin, Hufflepuff y Ravenclaw) a la que perteneces, de acuerdo a tus respuestas.

1) Iniciar test.

0) Salir.

Cualquier otro caso -> Opción no válida.

Para ello:

a) Realice al menos 5 preguntas al usuario. Puede utilizar las 7 aquí presentadas.

b) El orden de las respuestas presentadas no debe ser el mismo al repetir el test. Se recomienda combinar conjuntos, listas y diccionarios para este fin.

c) Utilice la lógica adecuada para determinar la casa con base en las respuestas.

d) Muestre la casa al final del test y finalice el programa.

'''
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
    opcion = int(input("Elige una opción: "))  #Opción del usuario.
    print("---------------------------------------------------")
    return opcion

# Función para hacer las preguntas del test y contar las respuestas
def hacer_test():
    # Lista de preguntas con sus opciones y las casas que corresponde.
    preguntas = [
        ("¿Qué preferirías que la gente no dijera de ti?",
         ["Ordinario (Gryffindor)", "Ignorante (Slytherin)", "Cobarde (Hufflepuff)", "Egoísta (Ravenclaw)"]),
        ("¿Qué te gustaría que hicieran al recordar tu nombre?",
         ["Te extrañen (Gryffindor)", "Cuenten tus historias (Slytherin)", "Admiren tus logros (Hufflepuff)", "No me importa (Ravenclaw)"]),
        ("¿Qué poción te gustaría inventar?",
         ["Gloria (Gryffindor)", "Poder (Slytherin)", "Amor (Hufflepuff)", "Sabiduría (Ravenclaw)"]),
        ("¿Cómo te describirías en una palabra?",
         ["Valiente (Gryffindor)", "Ambicioso (Slytherin)", "Leal (Hufflepuff)", "Curioso (Ravenclaw)"]),
        ("¿Qué cualidad te representa mejor?",
         ["Fuerza (Gryffindor)", "Astucia (Slytherin)", "Paciencia (Hufflepuff)", "Inteligencia (Ravenclaw)"])
    ]

    #Puntos para cada casa que los inicializo en 0.
    puntos_griffindor = 0
    puntos_slytherin = 0
    puntos_hufflepuff = 0
    puntos_ravenclaw = 0

    #Hace cada pregunta.
    for pregunta, opciones in preguntas:
        print(pregunta)  # Muestra la pregunta
        print("1)", opciones[0])  # Muestra la opción 1
        print("2)", opciones[1])  # Muestra la opción 2
        print("3)", opciones[2])  # Muestra la opción 3
        print("4)", opciones[3])  # Muestra la opción 4
        seleccion = int(input("Elige una opción: "))  #Aquí el usuario elige una opción y se guarda en(seleccion).

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

    #Calculo la casa ganadora.
    if puntos_griffindor > puntos_slytherin and puntos_griffindor > puntos_hufflepuff and puntos_griffindor > puntos_ravenclaw:
        casa = "Gryffindor"  #Si Gryffindor tiene más puntos, es la casa elegida.
    elif puntos_slytherin > puntos_griffindor and puntos_slytherin > puntos_hufflepuff and puntos_slytherin > puntos_ravenclaw:
        casa = "Slytherin"  #Si Slytherin tiene más puntos, es la casa elegida.
    elif puntos_hufflepuff > puntos_griffindor and puntos_hufflepuff > puntos_slytherin and puntos_hufflepuff > puntos_ravenclaw:
        casa = "Hufflepuff"  #Si Hufflepuff tiene más puntos, es la casa elegida.
    else:
        casa = "Ravenclaw"  #Si Ravenclaw tiene más puntos, es la casa elegida.

    #Mi resultado final.
    print("¡Felicidades! El sombrero seleccionador te ha asignado a la casa de:", casa)
    print("---------------------------------------------------")

#Ejecuta el test.
opcion = None#(-1)#Variable para almacenar la opción seleccionada.
while opcion != 0:  #Para hasta que el usuario seleccione la opción 0 (salir).
    opcion = mostrar_menu()  # Llama a la función que muestra el menú y obtiene la opción que ingreso el usuario.

    if opcion == 1:  #Si la opción es 1, inicia el test.
        hacer_test()  #Llama a la función que realiza el test.
    elif opcion == 0:  #Si la opción es 0,Fin de mi programa.
        print("Usted ha salido exitosamente del programa.Gracias por usar este programa y hacer el Test.")
        print("---------------------------------------------------")
    else:  #Por si la opción no es valida.
        print("Opción no válida.Por favor ingrese una opción entre 0 y 1.")
        print("---------------------------------------------------")
