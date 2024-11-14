print("****************************************")
print("****   Tania Garcia Flores.        *****")
print("****   12 de Noviembre de 2024.    *****")
print("****************************************")


print()
print("****** Vidoes de YT ******")
print()

lista=[]
opcion=-1
while opcion !=0:

    print("1)Ver lista de videos por añadidos")
    print("2) Muestra los videos por orden de la A-Z")
    print("3)Muestra los videospor orden de la Z-A ")
    print("4)Añadir video")
    print("5)Añadir varios videos")
    print("6)Eliminar video")
    print("0)Salir")
    print()
    opcion=int(input("ingrese su opcion:"))


    if opcion==1:
        print(lista)
        print("----------------------------------------------------")
        print()
    elif opcion == 2:
        lista.sort()
        for i in lista:
            print("----------------------------------------------------")
            print()
    elif opcion ==3:
        lista.sort(reverse=True)
        for u in lista:
            print(u)
            print("----------------------------------------------------")
            print()
    elif opcion == 4:
        numero=input("Ingrese su video")
        lista.insert(-1,numero)
        print("----------------------------------------------------")
        print()
    elif opcion == 5:
        numero=int(input("ingrese cuantos videos desea agregar"))
        i=1
        while i<= numero:
            ingresar=input("")
        print("----------------------------------------------------")
        print()
    elif opcion == 6:

        print("----------------------------------------------------")
        print()
