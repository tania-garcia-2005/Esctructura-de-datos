print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.   🍓🍓🍓🍓🍓")
print("🍓🍓                          🍓🍓🍓🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
######################################################################################
#Funcion para mostrar mi menú.
def menu():
    print("0) Salir.")
    print("1) Suma.")
    print("2) Resta.")
    print("3) Multiplicación.")
    print("4) División")
    print("5) División entera.")
    print("6) Exponenciación")
    opcion = int(input("Ingrese su opción: "))  # Recibe la opción elegida por el usuario y la convierte en entero.
    return opcion

#Función para la operación de suma.
def suma():
    numero_uno = float(input("Ingrese un número: "))
    numero_dos = float(input("Ingrese otro número: "))
    print(f"La suma de {numero_uno} y {numero_dos} es {numero_uno + numero_dos:.2f}.")
    print()

#Función para la operación de resta.
def resta():
    numero_uno = float(input("Ingrese un número: "))
    numero_dos = float(input("Ingrese otro número: "))
    print(f"La resta de {numero_uno} y {numero_dos} es {numero_uno - numero_dos:.2f}.")
    print()

#Función para la operación de multiplicación.
def multiplicacion():
    numero_uno = float(input("Ingrese un número: "))
    numero_dos = float(input("Ingrese otro número: "))
    print(f"La multiplicación de {numero_uno} y {numero_dos} es {numero_uno * numero_dos:.2f}.")
    print()

#Función para la operación de división.
def division():
    numero_uno = float(input("Ingrese un número: "))
    numero_dos = float(input("Ingrese otro número: "))
    print(f"La división entre {numero_uno} y {numero_dos} es: {numero_uno / numero_dos:.2f}.")
    print()

#Función para la operación de división entera.
def division_entera():
    numero_uno = float(input("Ingrese un número: "))
    numero_dos = float(input("Ingrese otro número: "))
    print(f"La división entera entre {numero_uno} y {numero_dos} es {numero_uno // numero_dos:.2f}.")
    print()

#Función para la operación de la exponenciación.
def exponenciacion():
    numero_uno = float(input("Ingrese un número: "))
    numero_dos = float(input("Ingrese otro número: "))
    print(f"La exponenciación de {numero_uno} a la {numero_dos} es {numero_uno ** numero_dos:.2f}.")
    print()


# En este apartado inicia  la parte de la función inicial.
print()
print()
print("-----------------------------------------------------------------")
print("****** ★彡『 𝓬𝓪𝓵𝓬𝓾𝓵𝓪𝓭𝓸𝓻𝓪 』彡★ ******")
print("-----------------------------------------------------------------")
print()
print()
opcion = None  # sustituye al -1,para inicializar la variable de la función.

while opcion != 0:  # Mientras el usuario no ingrese el número 0, el ciclo continuará
    opcion = menu()

    if opcion == 1:
        suma()
    elif opcion == 2:
        resta()
    elif opcion == 3:
        multiplicacion()
    elif opcion == 4:
        division()
    elif opcion == 5:
        division_entera()
    elif opcion == 6:
        exponenciacion()
    elif opcion == 0:
        print("Usted ha salido exitosamente del programa.")
    else:
        print("La opción no es válida. Intente de nuevamente por favor.")

