print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓Fecha: 20 de Noviembre de 2024     🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
'''''
Descripción:Este programa realiza una lista de las calificaciones y ejecuta cada opción establecida en el menú.. 

'''
print(" *** PROMEDIOS DEL PARCIAL 1 *** ")

# Lista para almacenar las calificaciones de los estudiantes.
calificaciones = []

#Materias
materias = ["ESTRUCTURA DE DATOS", "DERECHO Y LEGISLACIÓN", "CONTABILIDAD", "ELECTRÓNICA", "ÁLGEBRA"]
#Definicion de mi menú.
def menu():
    print("0) Salir")
    print("1) Ver calificaciones de alumno")
    print("2) Ver promedios de alumnos")
    print("3) Añadir alumno")
    print("4) Eliminar alumno")
    print("5) Ver promedio grupal")

    opcion = int(input("Ingrese su selección: "))
    return opcion
#opción para ver las calificaciones.
def ver_calificaciones():
    if len(calificaciones) == 0:
        print("No hay alumnos registrados.")
    else:
        nombre = input("Ingrese el nombre del alumno: ")
        encontrado = 0
        for alumno in calificaciones:
            if alumno["nombre"].lower() == nombre.lower():
                print(f"Calificaciones de {alumno["nombre"]}:")
                for materia in materias:
                    print(f"{materia}: {alumno["calificaciones"][materia]}")
                encontrado = 1
                break
        if encontrado != 1:
            print(f"Alumno {nombre} no encontrado.")
#opción para ver el promedio de los alumnos.
def promedio_alumnos():
    if len(calificaciones) == 0:
        print("No hay alumnos registrados.")
    else:
        print("Promedios de los alumnos:")
        for alumno in calificaciones:
            suma = 0
            for materia in materias:
                suma = suma + alumno["calificaciones"][materia]
            promedio = suma / len(materias)
            print(f"{alumno["nombre"]}: {promedio:.2f}")
#opción para añadir a un alumno.
def anadir_alumno():
    nombre = input("Ingrese el nombre del  alumno: ")
    existe = 0
    for alumno in calificaciones:
        if alumno["nombre"].lower() == nombre.lower():
            print(f"El alumno {nombre} ya está registrado.")
            existe = 1
            break

    if existe != 1:
        calificaciones_alumno = {}
        for materia in materias:
            valido = 0
            while valido == 0:
                cal = input(f"Ingrese la calificación de {materia}: ")
                if cal.isdigit() and 0 <= int(cal) <= 100:
                    calificaciones_alumno[materia] = int(cal)
                    valido = 1
                else:
                    print("Por favor ingrese un número válido entre 0 y 100.")
        calificaciones.append({"nombre": nombre, "calificaciones": calificaciones_alumno})
        print(f"Alumno {nombre} añadido exitosamente.")

#opción para eliminar un alumno.
def eliminar_alumno():
    if len(calificaciones) == 0:
        print("No hay alumnos registrados.")
    else:
        nombre = input("Ingrese el nombre del alumno que desea eliminar: ")
        conte= -1
        for u in range(len(calificaciones)):
            if calificaciones[u]["nombre"].lower() == nombre.lower():
                conte = u
                break
        if conte != -1:
            del calificaciones[conte]
            print(f"Alumno '{nombre}' eliminado exitosamente.")
        else:
            print(f"Alumno '{nombre}' no encontrado.")

#opción para ver el promedio grupal.
def promedio_grupal():
    if len(calificaciones) == 0:
        print("No hay alumnos registrados.")
    else:
        suma_materias = {materia: 0 for materia in materias}
        for alumno in calificaciones:
            for materia in materias:
                suma_materias[materia] += alumno["calificaciones"][materia]
        print("Promedio grupal especifico por cada materia:")
        for materia in materias:
            promedio = suma_materias[materia] / len(calificaciones)
            print(f"{materia}: {promedio:.2f}")
#Llamada de las funciones.
opcion = None

while opcion != 0:
    opcion = menu()
    if opcion == 1:
        ver_calificaciones()
    elif opcion == 2:
        promedio_alumnos()
    elif opcion == 3:
        anadir_alumno()
    elif opcion == 4:
        eliminar_alumno()
    elif opcion == 5:
        promedio_grupal()
    elif opcion == 0:
#mensajes.
        print("Usted ha salido del programa exitosamente")
    else:
        print("Opción inválida. Por favor, intente nuevamente.")



