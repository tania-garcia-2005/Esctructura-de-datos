#***************************************
#****   Tania Garcia Flores.      ******
#****   31 de octubre de 2024.    ******
#***************************************


print()
print("******PROGRAMA QUE CALCULA AREA PERIMETRO******")
print()


'''
Este programa determina el área y el perímetro de un rectángulo o de un círculo.
Muestre el siguiente menú:

1) Calcular el área de un rectángulo.
2) Calcular el perímetro de un rectángulo.
3) Calcular el área de un círculo.
4) Calcular el perímetro de un círculo.
0) Salir.
Cualquier otro caso -> Mostrar un mensaje de "opción no válida".

Para ello:

a) Muestre el menú anterior en consola.

b) En caso de calcular un área o perímetro, solicite al usuario los valores requeridos (flotantes).

c) Utilice la lógica adecuada para calcular lo solicitado. Asuma pi = 3.1416.

d) Imprima el resultado en la consola. Nota: muestre únicamente 3 decimales en todos los casos.

e) Repita el menú hasta salir.
'''
PI = 3.1416
contador = 1
while contador !=0:

    print("Menú:")
    print("1) Calcular el área de un rectángulo.")
    print("2) Calcular el perímetro de un rectángulo.")
    print("3) Calcular el área de un círculo.")
    print("4) Calcular el perímetro de un círculo.")
    print("0) Salir.")



    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = calcular_area_rectangulo= (base * altura)
        print(f"Área del rectángulo: {area:.3f}")
        print("--------------------------------")
    elif opcion == '2':
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        perimetro =2*(base* altura)
        print(f"Perímetro del rectángulo: {perimetro:.3f}")
        print("--------------------------------")
    elif opcion == '3':
        radio = float(input("Ingrese el radio del círculo: "))
        area = PI*(radio**2)
        print(f"Área del círculo: {area:.3f}")
        print("--------------------------------")
    elif opcion == '4':
        radio = float(input("Ingrese el radio del círculo: "))
        perimetro = 2* PI * radio
        print(f"Perímetro del círculo: {perimetro:.3f}")
        print("--------------------------------")
    elif opcion == '0':
        print("Saliendo del programa.")
        print()
        print("--------------------------------")

    else:
        print("Opción no válida. Intente nuevamente.")
        print("--------------------------------")