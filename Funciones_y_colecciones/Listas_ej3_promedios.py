print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓Fecha: 20 de Noviembre de 2024     🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
'''''
Descripción:Este programa realiza una lista de las calificaciones y ejecuta cada opción establecida en el menú.. 

'''

# Listas  para almacenar las calificaciones de los estudiantes.
Estructura_de_datos = []
Derecho = []
Contabilidad = []
Algebra = []
Electronica = []
Ingles = []
Calificaciones = [Estructura_de_datos, Derecho, Contabilidad, Algebra, Electronica,Ingles]
Posicion = 0
Opcion = None
#Definiciín de mi menú.
while Opcion != 0:
    print("🌸ξξ(∵❤◡❤∵)ξξ·¯·♩¸ *** promedios del parcial  *** ¸♩·¯·ξξ(∵❤◡❤∵)ξξ🌸")
    print()
    print("Bienvenido al menú de calificaciones")
    print("1) Ver calificaciones de alumno")
    print("2) Ver calificaciones de los alumnos")
    print("3) Añadir alumno")
    print("4) Eliminar alumno")
    print("5) Ver promedio grupal")
    print("0) Salir")
    print()
    Opcion = int(input("Ingresa una opción: "))
#Funciones para cumplir con cada punto del menú.
# Ejecuta la opción 1 del menú.
    if Opcion  == 1:
        print()
        if len(Estructura_de_datos) != 0:
             Numero_alumno = int(input("Ingrese el número del alumno que desea visualizar: "))
             print("Calificació|n del alumno ",Numero_alumno)
             print(f" Estructura de datos: {Estructura_de_datos[Numero_alumno]}.")
             print(f" Derecho: {Derecho[Numero_alumno]}.")
             print(f" Contabilidad: {Contabilidad[Numero_alumno]}.")
             print(f" Electronica: {Electronica[Numero_alumno]}.")
             print(f" Inglés: {Ingles[Numero_alumno]}.")
             print()
        else:
            print("No existen alumnos para ver")
    #Ejecuta la opción 2 del menú.
    elif Opcion == 2:
        print()
        if len(Estructura_de_datos) != 0:
            for Calificacion in Calificaciones:
                print(f" {Calificacion}")
        else:
            print("No hay alumnos por ver")
        print()
    # Ejecuta la opción 3 del menú.
    elif Opcion  == 3:
        print()
        print("Ingrese las calificaciones del alumno")
        Estructura_añdd = float(input("Estructuras de datos: "))
        Derecho_añdd = float(input("Derecho: "))
        Contabilidad_añdd = float(input("Contabilidad: "))
        Algebra_añdd = float(input("Algebra: "))
        Electronica_añdd = float(input("Electronica: "))
        Ingles_añdd = float(input("Inglés: "))

        Calificaciones[0].append(Estructura_añdd)
        Calificaciones[1].append(Derecho_añdd)
        Calificaciones[2].append(Contabilidad_añdd)
        Calificaciones[3].append(Algebra_añdd)
        Calificaciones[4].append(Electronica_añdd)
        Calificaciones[5].append(Ingles_añdd)
        print()
# Ejecuta la opción 4 del menú.
    elif Opcion  == 4:
        Eliminar_alumno = int(input("Ingrese el numero del alumno que deseas eliminar: "))
        del Estructura_de_datos[Eliminar_alumno]
        del Derecho[Eliminar_alumno]
        del Contabilidad[Eliminar_alumno]
        del Algebra[Eliminar_alumno]
        del Electronica [Eliminar_alumno]
        del Ingles[Eliminar_alumno]
    # Ejecuta la opción 5 del menú.
    elif Opcion == 5:
        if len(Estructura_de_datos) != 0:
            Numero_de_alumnos = len(Estructura_de_datos)
            Contador = 0
            Promedio_de_un_alumno = 0
            Total = 0
            while Contador < Numero_de_alumnos:
                #calculo de calificación.
                Promedio_de_un_alumno = (Estructura_de_datos[Contador] + Derecho[Contador] + Contabilidad[Contador] + Algebra[Contador] + Electronica[Contador] + Ingles[Contador])/6
                Total = Total + Promedio_de_un_alumno
                Contador += 1
            Total = Total / Numero_de_alumnos
            print("El promedio grupal es: ",Total)
        else :
            print()
            print("No hay alumnos para promediar")
        print()
    else:
        print()
        print("La opción es incorrecta")
        print()
# Ejecuta la opción 0 del menú(sale del programa).
if Opcion == 0:
    print()
    print("Usted ha salido del programa exitosamente")


