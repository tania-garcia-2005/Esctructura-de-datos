print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓Fecha: 20 de Noviembre de 2024     🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
'''''
Descripción:. 

'''

#calificacion de los alumnos.
Estructura_de_datos = []
Derecho = []
Contabilidad = []
Algebra = []
Electronica = []
Ingles = []
Calificaciones = [Estructura_de_datos, Derecho, Contabilidad, Algebra, Electronica,Ingles]
Posicion = 0
Opcion = None

while Opcion != 0:

    print("-------------------------------------------------------------------------------------------")
    print("****** 🌸ꗥ～ꗥ🌸  PROMEDIOS DEL PARCIAL  🌸ꗥ～ꗥ🌸 ******")
    print("-------------------------------------------------------------------------------------------")
    print()

    print("0) Salir")
    print("1) Ver calificaciones de alumno")
    print("2) Ver calificaciones de los alumnos")
    print("3) Añadir alumno")
    print("4) Eliminar alumno")
    print("5) Ver promedio grupal")
    print()
    Opcion = int(input("Ingresa una opción: "))
    if Opcion  == 0:
        print("Fin de programa")
    elif Opcion  == 1:
        print()
        if len(Estructura_de_datos) != 0:
             Numero_de_alumno = int(input("Ingrese el numero del alumno que deseas ver: "))
             print("Calificacion del alumno ",Numero_de_alumno)
             print(f" Estructura de datos: {Estructura_de_datos[Numero_de_alumno]}.")
             print(f" Derecho: {Derecho[Numero_de_alumno]}.")
             print(f" Contabilidad: {Contabilidad[Numero_de_alumno]}.")
             print(f" Electronica: {Electronica[Numero_de_alumno]}.")
             print(f" Ingles: {Ingles[Numero_de_alumno]}.")
             print()
        else:
            print("No hay alumnos por ver")
    elif Opcion == 2:
        print()
        if len(Estructura_de_datos) != 0:
            for Calificacion in Calificaciones:
                print(f" {Calificacion}")
        else:
            print("No hay alumnos por ver")
        print()

    elif Opcion  == 3:
        print()
        print("Ingrese las calificaciones del alumno")
        Estructura_añadido = float(input("Estructuras de datos: "))
        Derecho_añadido = float(input("Derecho: "))
        Contabilidad_añadido = float(input("Contabilidad: "))
        Algebra_añadido = float(input("Algebra: "))
        Electronica_añadido = float(input("Electronica: "))
        Ingles_añadido = float(input("Ingles: "))

        Calificaciones[0].append(Estructura_añadido)
        Calificaciones[1].append(Derecho_añadido)
        Calificaciones[2].append(Contabilidad_añadido)
        Calificaciones[3].append(Algebra_añadido)
        Calificaciones[4].append(Electronica_añadido)
        Calificaciones[5].append(Ingles_añadido)

        print()
    elif Opcion  == 4:
        Eliminar_de_alumno = int(input("Ingrese el numero del alumno que deseas eliminar: "))
        del Estructura_de_datos[Eliminar_de_alumno]
        del Derecho[Eliminar_de_alumno]
        del Contabilidad[Eliminar_de_alumno]
        del Algebra[Eliminar_de_alumno]
        del Electronica [Eliminar_de_alumno]
        del Ingles[Eliminar_de_alumno]

    elif Opcion == 5:
        if len(Estructura_de_datos) != 0:
            #Con una materia ya se sabe cuantos alumnos hay
            Numero_de_alumnos = len(Estructura_de_datos)
            Contador = 0
            Promedio_de_un_alumno = 0
            Total = 0
            while Contador < Numero_de_alumnos:
                #Si fuera la otra forma de lista , se podria utilizar la funcion sum
                Promedio_de_un_alumno = (Estructura_de_datos[Contador] + Derecho[Contador] + Contabilidad[Contador] + Algebra[Contador] + Electronica[Contador] + Ingles[Contador])/6
                Total = Total + Promedio_de_un_alumno
                Contador += 1
            Total = Total / Numero_de_alumnos
            print("El promedio grupal es: ",Total)
        else :
            print()
            print("No hay alumnos que promediar")
        print()
    else:
        print()
        print("Opción incorrecta")
        print()
print()
print("Salio del programa")




