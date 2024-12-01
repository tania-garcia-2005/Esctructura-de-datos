print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.   🍓🍓🍓🍓🍓")
print("🍓🍓                          🍓🍓🍓🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")

import random#Elije el ganador de forma aleatoria.

participantes = set()#Se utiliza para agregar(almacenar) a los participantes.
opcion = None#Sustituye al -1 para controlar las opciones del menú.

#Función para el mi menú.
while opcion != "0":
    print("----------------------------------------------------------------------------------")
    print("****** ★彡🎀RIFA DE UNA COMPUTADORA🎀』彡★ ******")
    print("----------------------------------------------------------------------------------")
    print()

    print("1) Ver correos")
    print("2) Agregar correo")
    print("3) Eliminar correo")
    print("4) Seleccionar ganador")
    print("0) Salir")

    opcion = input("Elige una opción: ") #opción del usuario.
#función para ver los correos.
    if opcion == "1":
        if len(participantes) > 0:
            print("El conjunto de correos registrados es:")
            for correo in participantes:
                print(f" - {correo}")
        else:
            print("No hay participantes registrados.")
#función para agregar los correos.
    elif opcion == "2":
        correo = input("Ingresa el correo: ").strip()
        if correo in participantes:
            print("Este correo ya está registrado.")
        else:
            participantes.add(correo)
            print("Correo agregado.")
#función para eliminar  correos.
    elif opcion == "3":
        correo = input("Ingresa el correo que desea eliminar: ").strip()
        if correo in participantes:
            participantes.remove(correo)
            print("El correo se ha eliminado exitosamente.")
        else:
            print("El correo que usted ha ingresado no está registrado.")
#función para seleccionar ganador.
    elif opcion == "4":
        # Verificamos que existan participantes.
        if len(participantes) > 0:
            lista_participantes = list(participantes)# Convertí el conjunto a una lista(elije un ganador aleatoriamente).
            ganador = random.choice(lista_participantes)
            print(f"El ganador es: {ganador}.Muchas Felicidades!")
        else:
            print("No existen participantes registrados.")
#Si el usuario ingresa la opción cero sale del programa.
    elif opcion == "0":
        print("Usted ha salidonexistosamente del  programa.")
    else:
        print("Su opción no es  válida. Por favor, intente nuevamente.")