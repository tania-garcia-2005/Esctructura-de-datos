from errno import ELOOP

print("****************************************")
print("****   Tania Garcia Flores.        *****")
print("****   13 de Noviembre de 2024.    *****")
print("****************************************")

'''''
Descripción:Añadir promedios. 

'''

print()
print("******promedios del parcial 1 ******")
print()




calificaciones=[]
materias = ["ESTRUCTURA DE DATOS", "DERECHO Y LEGISLACIÓN", "CONTABILIDAD", "ELECTRÓNICA", "ÁLGEBRA"]#Estas son las calificaciones que se ocupan.

def menu():


    print("1)Ver calificacion del alumno")
    print("2) Ver promedios de alumno")
    print("3)añadir alumno")
    print("4)Eliminar alumno")
    print("5Eliminar alumno")
    print("6)Ver promedio grupal")
    print("0)Salir")
    print()
    opcion = int(input("ingrese su opcion:"))

    return opcion

#calificacion de los alumnos.
def ver_calificaciones_alumno():
    if len(calificaciones) == 0:
        print("No existen alumnos registrados.")
    else:
        nombre = input("Ingrese el nombre del alumno: ")
        encontrado = False
        for alumno in calificaciones:
            if alumno["nombre"].lower() == nombre.lower():
                print(f"\nCalificaciones de {alumno['nombre']}:")
                for materia in materias:
                    print(f"{materia}: {alumno['calificaciones'][materia]}")
                encontrado = True
                break
        if encontrado == False:
            print(f"Alumno '{nombre}' no encontrado.")

#promedios
def ver_promedios_alumnos():
    if len(calificaciones) == 0:
        print("No hay alumnos registrados.")
    else:
        print("\nPromedios de los alumnos:")
        for alumno in calificaciones:
            suma = 0
            #revisarrr
            for materia in materias:
                suma += alumno["calificaciones"][materia]
            promedio = suma / len(materias)
            print(f"{alumno['nombre']}: {promedio:.2f}")

#alumnoo
def anadir_alumno():
    nombre = input("Ingrese el nombre del nuevo alumno: ")
    #existe?
    existe = False
    for alumno in calificaciones:
        if alumno["nombre"].lower() == nombre.lower():
            print(f"El alumno '{nombre}' ya está registrado.")
            existe = True
            break
    if existe == False:
        calificaciones_alumno = {}
        for materia in materias:
            valido = False
            while valido == False:
                cal = input(f"Ingrese la calificación de {materia}: ")
                if cal.isdigit() and 0 <= int(cal) <= 100:
                    calificaciones_alumno[materia] = int(cal)
                    valido = True
                else:
                    print("Ingrese un número válido entre 0 y 100.")
        calificaciones.append({"nombre": nombre, "calificaciones": calificaciones_alumno})
        print(f"Alumno '{nombre}' añadido exitosamente.")


def ver_promedio_grupal():
    if len(calificaciones) == 0:
        print("No hay alumnos registrados.")
    else:
        suma_materias = {materia: 0 for materia in materias}
        for alumno in calificaciones:
            for materia in materias:
                suma_materias[materia] += alumno["calificaciones"][materia]
        print("\nPromedio grupal por materia:")
        for materia in materias:
            promedio = suma_materias[materia] / len(calificaciones)
            print(f"{materia}: {promedio:.2f}")


opcion = -1
while opcion != 0:
    opcion = menu()
    if opcion == 1:
        ver_calificaciones_alumno()
    elif opcion == 2:
        ver_promedios_alumnos()
    elif opcion == 3:
        anadir_alumno()
    elif opcion == 4:
        eliminar_alumno()
    elif opcion == 5:
        ver_promedio_grupal()
    elif opcion == 0:
        print("")
    else:
        print("La opción no es valida Por favor, intente nuevamente.")




