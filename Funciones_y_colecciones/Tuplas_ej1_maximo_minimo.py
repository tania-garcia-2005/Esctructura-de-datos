print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓Fecha: 25 de Noviembre de 2024     🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("-------------------------------------------------------------------------------------------------------------------------------------")
print()
'''
Descripción: Este programa muestra el valor máximo y mínimo de una lista de números. En este caso, la tupla se utiliza para devolver los valores máximo y mínimo de la función.
'''


###################################################################################################

# Definición del menú
def menu():
    print("🌸ξξ(∵❤◡❤∵)ξξ·¯·♩¸ ***  Valor máximo y mínimo de una lista de números del usuario  *** ¸♩·¯·ξξ(∵❤◡❤∵)ξξ🌸")
    print(
        "-------------------------------------------------------------------------------------------------------------------------------------")
    print()
    print("1) Ver lista de números")
    print("2) Añadir número a la lista")
    print("3) Determinar el valor máximo y mínimo de la lista de números")
    print("0) Salir")
    print()
    opcion = int(input("Ingrese su opción: "))
    return opcion

#Etsa función esta encargada de mostras la lista de números y en caso de que la lista no tenga números imprime un mensaje indicando que no hay números.
def muestra(lista):
    if lista:
        print(f"La lista de números es: {lista}")
    else:
        print("La lista no tiene ningún contenido.")
    print()

#La funcion agrega los números nuevos a la lsita inicial.
def agregar(lista):
    nuevo_nmr = float(input("Ingrese el número que desea agregar a la lista: "))
    lista.append(nuevo_nmr)
    print("El número ha sido agregado correctamente")
    print()

#Identifica que número de la lista es el máximo y mínimo (mayor o menor).
def determina(lista):
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    menor = lista[0]
    for x in lista:
        if x < menor:
            menor = x
    return (mayor, menor)


#Eta es la lista de iniciación vacía.
lista = []

#llamada del menú principal.
opcion_usuario = None
while opcion_usuario != 0:
    opcion_usuario = menu()

    if opcion_usuario == 1:
        muestra(lista)

    elif opcion_usuario == 2:
        agregar(lista)

    elif opcion_usuario == 3:
        if lista:
            tupla = tuple(lista)
            mas, menos = determina(lista)
            print(f"El número mayor es: {mas} y el número menor es: {menos}")
            print()
        else:
            print("La lista está vacía")
            print()

    elif opcion_usuario > 3:
        print("La opción no es válida.")

    elif opcion_usuario == 0:
        print("Usted ha salido exitosamente del programa.")

