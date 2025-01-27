"""
Descripción:
En este archivo se valida que la entrada por consola sea la adecuada, por ejemplo, verificando que efectivamente
sea un número cuando se solicita.
"""


# Forma de solicitar un número de la forma actual:
print("Forma actual de solicitar un número.")

prueba_numero = int(input("Ingresa un número: "))
print()


# Sin embargo, genera un error de tipo ValueError si no se ingresa un número.
# Una solución consiste en verificar que lo ingresado efectivamente sea un número.
print("Funciones que pueden servir con cadenas.")

cadena = input("Ingresa una cadena: ")
print(f"isnumeric(): {cadena.isnumeric()}")
print(f"isalpha(): {cadena.isalpha()}")
print(f"isalnum(): {cadena.isalnum()}")
print()


# Lo anterior se puede aprovechar para verificar que un número sea correcto, por ejemplo, para elegir
# la opción correcta dentro de un menú.
print("Verificando restricciones de números.")

numero = input("Ingresa el número cero o un número entero positivo para continuar: ")

while not numero.isnumeric():
    print("Opción no válida, intenta nuevamente.")
    print()
    numero = input("Ingresa el número cero o un número entero positivo para continuar: ")

# El número ingresado ahora se convierte a tipo int.
print()
numero = int(numero)
print(f"El número convertido a entero es: {numero}")
print(f"El tipo de dato es: {type(numero)}")
print()


# Un detalle del código anterior es que pudiera no funcionar con enteros negativos.
# Una manera de solventarlo sería la siguiente (utilizando una función para reutilizar el código más adelante).
def cadena_a_entero(cadena):
    no_guiones = cadena.count("-")
    revisar_cadena =cadena.lstrip('-')

    if revisar_cadena.isnumeric() and no_guiones in (0, 1):
        return int(cadena)
    else:
        return None

print("Conversión de cadena a entero con verificación.")

num_cadena = input("Ingresa un número entero: ")
numero = cadena_a_entero(num_cadena)

while numero is None:
    print("Opción no válida, intenta nuevamente.")
    print()

    num_cadena = input("Ingresa un número entero: ")
    numero = cadena_a_entero(num_cadena)

# El número ingresado ahora es de tipo int.
print()
print(f"El número convertido a entero es: {numero}")
print(f"El tipo de dato es: {type(numero)}")
print()


# De manera similar, se verifica si un número es de tipo flotante.
def cadena_a_flotante(cadena):
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena =cadena.lstrip('-').replace(".","")

    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None

print("Conversión de cadena a flotante con verificación.")

num_cadena = input("Ingresa un número flotante: ")
numero = cadena_a_flotante(num_cadena)

while numero is None:
    print("Opción no válida, intenta nuevamente.")
    print()

    num_cadena = input("Ingresa un número flotante: ")
    numero = cadena_a_flotante(num_cadena)

# El número ingresado ahora es de tipo float.
print()
print(f"El número convertido a float es: {numero}")
print(f"El tipo de dato es: {type(numero)}")
print()
