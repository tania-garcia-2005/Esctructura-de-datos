print("****************************************")
print("****   Tania Garcia Flores.        *****")
print("****   14 de Noviembre de 2024.    *****")
print("****************************************")

'''''
Descripción:Añadir producto a la lista de compras. 

'''


def menu ():

    print("1)Ver lista")
    print("2)Añadir producto a la lista")#nombre y cantidad
    print("3)Eliminar producto de lista")
    print("0)Salir")

    print()
    opcion = int(input("ingrese su opción:"))

    return opcion

def  añadir_producto(lista_de_compras):

    print()
###################################################################
print()
print("****** Lista de compras ******")
print()

lista = []
opcion = None  # None sustituye al -1,para tener una variable opuesta a tu condiicioon del while(no tiene ningun valro)
while opcion!=0:
    opcion = menu()


    if opcion==1:
        print(lista)
        print("----------------------------------------------------")
        print()
    elif opcion == 2:
        nombre=input("nombre del producto")#ingresa el nombre del producto
        cantidad=input("cantidad del producto")#ingresa la cantidad del producto

        producto=[nombre,cantidad]#
        lista.append(producto)
        print("----------------------------------------------------")
        print()

    elif opcion ==3:
        print()
    elif opcion ==
         print()
        numero=int(input("ingrese su cantidad"))
        i=1
    while i<= numero:
        ingresar=input("")
    print("----------------------------------------------------")
    print()



#tengo 2 listas con 2 indices y tengo que ver cpomo borarr las listas para eliminar un rpoducto
