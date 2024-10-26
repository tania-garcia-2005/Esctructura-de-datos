#***************************************
#****   Tania Garcia Flores.      ******
#****   26 de octubre de 2024.    ******
#***************************************

'''''
Descripción:
Este programa determinará cuál de dos números ingresados por el usuario es menor o si son iguales.
'''

print()
print("******Cuál de dos números ingresados es menor o si son iguales ******")#Título.
print()

#Solicita 2 numeros.
#Convierte a flotantes.
numero1=float(input("Ingrese su primer número: "))
numero2=float(input("Ingrese su segundo número: "))

#Realiza las comparaciónes e imprime que número es el menor o si son iguales.
if numero1<numero2:
    print("Su primer número es menor al segundo número ")
elif numero1>numero2:
    print("Su segundo número es menor a su primer número ")
else:
    print("Los números son iguales")