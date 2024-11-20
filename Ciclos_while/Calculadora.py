print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.   🍓🍓🍓🍓🍓")
print("🍓🍓                          🍓🍓🍓🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")

'''''
Descripción:Este programa realiza una calculadora básica. 
.

'''

###################################################################
print("-----------------------------------------------------------------")
print("****** ★彡『 𝓬𝓪𝓵𝓬𝓾𝓵𝓪𝓭𝓸𝓻𝓪 』彡★ ******")
print("-----------------------------------------------------------------")
print()
print()



opcion = None
while opcion != 0:

    print("0) Salir.")
    print("1) Suma.")
    print("2) Resta.")
    print("3) Multiplicación.")
    print("4) División")
    print("5) División entera.")
    print("6) Exponenciación.")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La suma de {numero_uno} y {numero_dos} es {numero_uno + numero_dos:.2f}.")
        print()
    elif opcion == 2:
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La resta de {numero_uno} y {numero_dos} es {numero_uno - numero_dos:.2f}.")
        print()
    elif opcion == 3:
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La multiplicación de {numero_uno} y {numero_dos} es {numero_uno * numero_dos:.2f}.")
        print()
    elif opcion == 4:
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        if numero_dos != 0:
            print(f"La división entre {numero_uno} y {numero_dos} es: {numero_uno / numero_dos:.2f}.")
        else:
            print("Error: No se puede dividir entre cero.")
        print()
    elif opcion == 5:
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        if numero_dos != 0:
            print(f"La división entera entre {numero_uno} y {numero_dos} es {numero_uno // numero_dos:.2f}.")
        else:
            print("Error: No se puede dividir entre cero.")
        print()
    elif opcion == 6:  # Corrige el número de opción para exponenciación
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La exponenciación de {numero_uno} a la {numero_dos} es {numero_uno ** numero_dos:.2f}.")
        print()
    elif opcion == 0:
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Intente de nuevo.")