#***************************************
#****   Tania Garcia Flores.      ******
#****   26 de octubre de 2024.    ******
#***************************************


'''
Descripción:
Ejemplos de uso de los operadores aritméticos.
'''

"""
Los operadores aritméticos en Python son los siguientes:
- Suma (+).
- Resta (-).
- Multiplicación (*).
- División (/).
- División entera (//).
- Módulo (%).
- Exponenciación (**).
"""

# Se solicitan dos números enteros al usuario.

numero1 = int(input("Ingresa un número entero: "))
numero2 = int(input("Ingresa otro número entero: "))

# Se realizan las operaciones aritméticas.
print()
print("  ***   Ejemplos de uso de los operadores aritméticos   ***")

print(f"La suma de ({numero1} + {numero2}) es: {numero1 + numero2}")#Imprime el resultado de la suma de el numero1 con el numero2.
print(f"La resta de ({numero1} - {numero2}) es: {numero1 - numero2}")#Imprime el resultado de la resta de el numero1 con el numero2.
print(f"La multiplicación de ({numero1} * {numero2}) es: {numero1 * numero2}")#Imprime el resultado de la multi´plicación de el numero1 con el numero2.
print(f"La división de ({numero1} / {numero2}) es: {(numero1 / numero2):.2f}")#Imprime el resultado de la división de el numero1 con el numero2y muestra solo dos decimales.
print(f"La división entera de ({numero1} // {numero2}) es: {numero1 // numero2}")#Imprime el resultado de la división entera de el numero1 con el numero2.
print(f"El módulo de ({numero1} % {numero2}) es: {numero1 % numero2}")#Imprime el resultado de el módulo de el numero1 con el numero2.
print(f"La exponenciación  de ({numero1} ** {numero2}) es: {numero1 ** numero2}")#Imprime el resultado de la exponenciación de el numero1 con el numero2.


