numero1_cadena = input("Introduce un número decimal: ")
numero2_cadena = input("Introduce otro número decimal: ")
resultado_cadena = numero1_cadena + numero2_cadena # Verificar qué es lo que realiza esta instrucción (ver el print).
print()
print(" **  Recibir número sin un casting de varibles  **")
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}")



# Comentar por qué se realiza el casting de variables.


numero1_float = float(numero1_cadena)
numero2_float = float(numero2_cadena)
resultado_float = numero1_float + numero2_float
print()
print(" **  Casting de varibles  **")
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")