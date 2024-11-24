print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.   🍓🍓🍓🍓🍓")
print("🍓🍓7 de noviembre  de 2024   🍓🍓🍓🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")

'''''
Descripción:Este programa realiza una piramide utilizando funciones en phyton. 
.
'''
# Esta función muestra  el menú.
def menu():
    print("----------------------------------------------------------------------------------")
    print("****** ★彡🎀『 【p】【i】【r】【a】【m】【i】【d】【e】🎀』彡★ ******")
    print("----------------------------------------------------------------------------------")
    print()

    print("Bienvenido al menú de los triángulos")
    print("0) Salir.")
    print("1) Primer triángulo.")
    print("2) Segundo triángulo.")
    print("3) Tercer triángulo.")
    print("4) Cuarto triángulo.")
    opcion = int(input("Ingrese su opción: "))  # Recibe la opción elegida por el usuario y la convierte en entero.
    return opcion

#Función del primer triángulo.
def triangulo_1():
    fila = int(input("Ingrese el número de filas que desee: "))
    fila1 = fila
    contador = fila

    print("Primer triángulo")
    for u in range(1, fila1 + 1):
        asteriscos = " * " * u  # Multiplico el asterisco por la u de mi for implementado.
        print(f" {asteriscos}")
    print()

##Función del segundo triángulo.
def triangulo_2():
    fila = int(input("Ingrese el número de filas que desee: "))
    fila1 = fila
    contador = fila

    print("Segundo triángulo")
    for y in range(1, fila + 1):
        asteriscos = " * " * fila
        fila = fila - 1
        print(f" {asteriscos}")
    print()

#Función del tercer triángulo.
def triangulo3():
    print("Tercer triángulo")
    fila = int(input("Ingrese el número de filas que desee: "))
    filauno = fila
    contador = 0
    for y in range(1, fila + 1):
        espacio = " " * (fila - y)
        asteriscos = "*" * (contador + 1)
        contador += 2
        print(f" {espacio}{asteriscos}")
        print()

#Función del cuarto triángulo.
def triangulo4():
    print("Cuarto triángulo")
    fila = int(input("Ingrese el número de filas que desee: "))
    filauno = fila
    contador = 0
    for z in range(1, filauno + 1):
        print(" " * (filauno - z) + "*" * z)
        print()

##################################################################
print("*** Bienvenido al  menú de triángulos ***")

opcion_elegida = None  #sustituye al -1 para inicializar.

while opcion_elegida != 0:  #Mientras el usuario no ingrese el número 0, el ciclo continuará.
    opcion_elegida = menu()  # Llamada a la función menu().

    if opcion_elegida == 1:
        triangulo_1()
    elif opcion_elegida == 2:
        triangulo_2()
    elif opcion_elegida == 3:
        triangulo3()
    elif opcion_elegida == 4:
        triangulo4()
    elif opcion_elegida > 0:
        print("Opción inválida")
        print()

print("Usted ha salido exitosamente del programa ")