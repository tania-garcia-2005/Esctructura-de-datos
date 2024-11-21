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

##Declaración del menú correspondiente.

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
    #operaciones

    if opcion == 1:  # Este punto ejecuta la Opción 1 suma.
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La suma de {numero_uno} y {numero_dos} es {numero_uno + numero_dos:.2f}.")
        print()
    elif opcion == 2:  #Este punto ejecuta la Opción 2 resta.
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La resta de {numero_uno} y {numero_dos} es {numero_uno - numero_dos:.2f}.")
        print()
    elif opcion == 3:  #Este punto ejecuta la Opción 3 multiplicación.
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La multiplicación de {numero_uno} y {numero_dos} es {numero_uno * numero_dos:.2f}.")
        print()
    elif opcion == 4:  #Este punto ejecuta la Opción 4 división
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La división entre {numero_uno} y {numero_dos} es: {numero_uno / numero_dos:.2f}.")
        print()
    elif opcion == 5:  #Este punto ejecuta la Opción 5 división entera
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La división entera entre {numero_uno} y {numero_dos} es {numero_uno // numero_dos:.2f}.")
        print()
    elif opcion == 6:  #Este punto ejecuta la Opción 6 exponenciación
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La exponenciación de {numero_uno} a la {numero_dos} es {numero_uno ** numero_dos:.2f}.")
        print()

    elif opcion == 0:
        print("Usted ha salido exitosamente del programa.")
    else:
        print("La opción no es válida. Intente de nuevamente por favor.")