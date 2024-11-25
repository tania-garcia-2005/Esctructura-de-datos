print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.   🍓🍓🍓🍓🍓")
print("🍓🍓                          🍓🍓🍓🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")

'''''
Descripción: Este programa crea una lista de compras.
'''

# Función para mi menú.
def menu():  # Definición del menú
    print("1) Ver lista")
    print("2) Añadir producto a la lista")  # nombre y cantidad
    print("3) Eliminar producto de lista")
    print("0) Salir")

    print()
    opcion = int(input("Ingrese su opción:"))

    return opcion

def añadir_producto(lista_de_compras):
    print()

###################################################################
print()
print("-----------------------------------------------------------------")
print("****** ★彡『 LISTA DE COMPRAS 』彡★ ******")
print("-----------------------------------------------------------------")
print()

lista = []
opcion = None  # None sustituye al -1, para tener una variable opuesta a tu condición del while (no tiene ningún valor)
while opcion != 0:
    opcion = menu()

    if opcion == 1:
        print(lista)
        print("----------------------------------------------------")
        print()
    elif opcion == 2:
        nombre = input("Nombre del producto:")  # Ingresa el nombre del producto
        cantidad = input("Cantidad del producto:")  # Ingresa la cantidad del producto

        producto = [nombre, cantidad]  # Crea un producto con nombre y cantidad
        lista.append(producto)
        print("----------------------------------------------------")
        print()

    elif opcion == 3:
        print("Lista ")
        contador = 0
        for producto in lista:
            print(f"{contador}) {producto[0]} -->> Cantidad: {producto[1]}")
            contador= contador + 1
        borrar = int(input("Ingrese el número del producto a eliminar: "))
        if borrar > contador:
            print(f"No hay {contador} productos")
            print("------------------------------")
            print()
        else:
            borrar = borrar
            lista.pop(borrar)
            contador = contador - 1
            print("El producto ha sido eliminado correctamente.")

print("Usted ha  salido del programa exitosamente.")
print()
print("------------------------------")
print()
print("Agradezco que halla utilizado este programa")
