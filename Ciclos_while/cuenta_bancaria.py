print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓Fecha: 29 de octubre de 2024     🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")

'''''
Descripción: Este programa es un ejercicio sobre los ciclos while
'''

###################################################################
print("-----------------------------------------------------------------")
print("****** ★彡『 𝐵𝒶𝓃𝒸𝑜 𝒜𝓏𝓉𝑒𝒸𝒶 』彡★ ******")
print("-----------------------------------------------------------------")
print()
print()

#Declaraciones.
opciones = -1
saldo = 0
#condición.
while opciones != 0:
    #Menú.
    print("Bienvenido al menú de Banco Azteca")
    print("0) Salir.")
    print("1) Consultar saldo.")
    print("2) Ingresar dinero.")
    print("3) Retira dinero.")
    opciones = int(input("Ingrese su selección: "))
    # condiciónes.
    if opciones == 1:
        print(f"Su saldo es de: {saldo:.2f}")
        print()
    elif opciones == 2:
        cash = float(input("Ingrese la canidad que desea depositar: "))#
        saldo = saldo + cash#suma la cantidad ingresada + su saldo.
        print("Dinero depositado correctamente")
        print()
    elif opciones == 3:
        sacar = float(input("Ingrese la canidad que desea retirar: "))
        if sacar > saldo:#solo si el saldo es mayor al dinero que desea retirar.
            print("Lo sentimos su dinero  es INSUFICIENTE ")
            print()
        else:
            saldo = saldo - sacar
            print("Dinero retirado correctamente")
            print()
    else:
        print("Opción inválida")
        print()