#***************************************
#****   Tania Garcia Flores.      ******
#****   29 de octubre de 2024.    ******
#***************************************

'''''
Descripción:
pide la edad y determina si es mayor de edad
'''

''''
#MENU
0)salir
1)suma
2)resta
3)multiplicacion
4)diviision
5)division entera
6)exponenciacion
'''

print()
print("******CALCULADORA BÁSICA******")#Título.
print()
opcion=-1
while opcion !=0:
    print("0) salir")
    print("1) suma")
    print("2) resta")
    print("3) multiplicación")
    print("4) División")
    print("5) Division entera")
    print("6) Exponenciación")

    ingresa=int(input("Ingrese una opción: "))

    if ingresa==1:
        numero1,numero2=float(input("Ingrese un numero: ")),float(input("Ingrese otro numero: "))
        print(f"La suma de ({numero1} + {numero2}) es: {numero1 + numero2:.2f}")
    elif ingresa==2:
        numero1, numero2 = float(input("Ingrese un numero: ")), float(input("Ingrese otro numero: "))
        print(f"La resta de ({numero1} - {numero2}) es: {numero1 - numero2:.2f}")
    elif ingresa==3:
        numero1, numero2 = float(input("Ingrese un numero: ")), float(input("Ingrese otro numero: "))
        print(f"La multiplicación de ({numero1} * {numero2}) es: {numero1 * numero2:.2f}")
    elif ingresa==4:
        numero1, numero2 = float(input("Ingrese un numero: ")), float(input("Ingrese otro numero: "))
        print(f"La división de ({numero1} / {numero2}) es: {(numero1 / numero2):.2f}")
    elif ingresa==5:
        numero1, numero2 = float(input("Ingrese un numero: ")), float(input("Ingrese otro numero: "))
        print(f"La división entera de ({numero1} // {numero2}) es: {numero1 // numero2:.2f}")
    elif ingresa==6:
        numero1, numero2 = float(input("Ingrese un numero: ")), float(input("Ingrese otro numero: "))
        print(f"La exponenciación  de ({numero1} ** {numero2}) es: {numero1 ** numero2:.2f}")
    else:
        print("La opción no es valida :(")
        print()


    print("TERMINO LA PRIMER OPERACIÓN")
    print()
    print("CALCULADORA " )






