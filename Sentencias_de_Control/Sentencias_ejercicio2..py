#***************************************
#****   Tania Garcia Flores.      ******
#****   26 de octubre de 2024.    ******
#***************************************

'''''
Descripción:
Este programa determinará la estación del año de acuerdo al número de mes ingresado por el usuario.
'''

print()
print("****** Programa que determina la estación del año ******")#Título.
print()

'''
    a) Solicite al usuario un número que representa al mes.
    b) Utilice la lógica adecuada para determinar la estación del año de acuerdo con:
    3, 4 y 5: Primavera.
    6, 7 y 8: Verano.
    9,10 y 11: Otoño.
    12, 1 y 2: Invierno.
    Otro caso: Mensaje de mes incorrecto.
    c) Muestre la estación correspondiente en consola.
'''
numero=int(input("ingrese el número del mes: "))

#Realiza las comparaciones utilizando el operador lógico OR
if numero==3 or numero==4 or numero==5:
    print("Primavera")
elif numero==6 or numero==7 or numero==8:
    print("Verano")
elif numero==9 or numero==10 or numero==11:
    print("Otoño")
elif numero==12 or numero==1 or numero==2:
    print("Invierno")
else:
    print("Mes incorrecto")#Si no se cumple ninguna de las condiciones anteriores el mensaje que imprimirá será: Mes incorrecto.

