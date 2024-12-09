"""
Descripción del programa:

Este programa convierte números entre las bases decimal, binaria y hexadecimal.
Muestra el siguiente menú:

***Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***

1) Convertir de decimal a binario y hexadecimal.

2) Convertir de binario a decimal y hexadecimal.

3) Convertir de hexadecimal a decimal y binario.

0) Salir.

Cualquier otro caso -> Opción no válida.

Para ello:

a) Utilice la lógica adecuada para mostrar las conversiones. No utilice funciones como bin() o hex().

b) Asuma que el usuario siempre va a ingresar números en el formato adecuado. Por ejemplo: 1001 como número binario o 1F como hexadecimal, no 120 como número binario o 1Z como hexadecimal.

c) Para considerar el ejercicio como completo, utilice funciones para mostrar el menú y para las conversiones entre bases, considerando que cada función devuelve una tupla. Por ejemplo, la función que recibe el número decimal debe devolver el valor en binario y en hexadecimal como una tupla.

"""
# Mi portada.
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓                                🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print()
print("----------------------------------------------------------------------------------")
print()

# Mi portada.
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓                                🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print()
print("----------------------------------------------------------------------------------")
print()

# Función
def convertir_a_binario(numero_decimal):
    # Mi cadena vacía para guardar el número en binario.
    resultado_binario = ""
    valor = numero_decimal

    # Convertí el número decimal a binario dividiendo entre el número 2.
    if valor == 0:  # Si el número es 0, el binario también es "0".
        resultado_binario = "0"

    while valor > 0:
        residuo = valor % 2  # Obtengo el residuo (0 o 1).
        resultado_binario = str(residuo) + resultado_binario  # Agrega el residuo al inicio.
        valor = valor // 2  # Aquí divide el número entre el número 2.

    return resultado_binario

def convertir_a_hexadecimal(numero_decimal):
    # Cadena vacía que guardar el número en hexadecimal.
    resultado_hexadecimal = ""
    caracteres_hex = "0123456789ABCDEF"  # Estos son mis valores hexadecimales.
    valor = numero_decimal

    # Aquí se convierte el número decimal a hexadecimal dividiendo entre el número 16.
    if valor == 0:  # Si el número es 0, el hexadecimal también es "0".
        resultado_hexadecimal = "0"

    while valor > 0:
        residuo = valor % 16  # Se obtiene el residuo (0-15).
        resultado_hexadecimal = caracteres_hex[residuo] + resultado_hexadecimal
        valor = valor // 16  # Aquí se divide el número entre el número 16.

    return resultado_hexadecimal

def convertir_a_decimal_desde_binario(cadena_binaria):
    # Inicializa el resultado decimal desde el número 0.
    resultado_decimal = 0
    exponente = 0

    # Se convierte de binario a decimal sumando las potencias del número 2.
    for i in range(len(cadena_binaria) - 1, -1, -1):  # Aquí se recorre mi binario de derecha a izquierda.
        if cadena_binaria[i] == "1":  # Si el dígito es 1, suma la potencia del número 2.
            resultado_decimal += 2 ** exponente
        exponente += 1  # Incrementa la potencia(i++).
    return resultado_decimal

def convertir_a_hexadecimal_desde_binario(cadena_binaria):
    # Convierte primero el binario a decimal, luego a hexadecimal.
    decimal = convertir_a_decimal_desde_binario(cadena_binaria)
    return convertir_a_hexadecimal(decimal)

def convertir_a_decimal_desde_hexadecimal(cadena_hexadecimal):
    # Mi tabla de valores hexadecimales.
    caracteres_hex = "0123456789ABCDEF"
    resultado_decimal = 0
    exponente = 0

    # Convierte el hexadecimal a decimal
    for i in range(len(cadena_hexadecimal) - 1, -1, -1):  # Recorre el hexadecimal de derecha a izquierda.
        valor = caracteres_hex.index(cadena_hexadecimal[i])  # Busca el valor del dígito en la tabla.
        resultado_decimal += valor * (16 ** exponente)  # Suma el valor del dígito por la potencia del número 16.
        exponente += 1
    return resultado_decimal

def convertir_a_binario_desde_hexadecimal(cadena_hexadecimal):
    # Convierte el hexadecimal a binario.
    decimal = convertir_a_decimal_desde_hexadecimal(cadena_hexadecimal)
    return convertir_a_binario(decimal)

def mostrar_menu_principal():
    # Función de mi menú.
    print("`•.,¸¸,.•´¯🎀🌸CONVERSIÓN ENTRE SISTEMAS NÚMERICOS🌞🎀¯´•.,¸¸,.•`")
    print()
    print("1) Convertir de decimal a binario y hexadecimal.")
    print("2) Convertir de binario a decimal y hexadecimal.")
    print("3) Convertir de hexadecimal a decimal y binario.")
    print("0) Salir.")
    seleccion = int(input("Ingresa una de las opciones: "))
    print("---------------------------------------------------")
    print()
    return seleccion

opcion_seleccionada = None
while opcion_seleccionada != 0:
    opcion_seleccionada = mostrar_menu_principal()

    if opcion_seleccionada == 0:
        # Fin de mi programa.
        print("Usted ha salido exitosamente del programa, ¡Hasta luego!")

    elif opcion_seleccionada == 1:
        # Convierte de decimal a binario y hexadecimal.
        numero_decimal = int(input("Ingresa un número decimal: "))
        binario = convertir_a_binario(numero_decimal)
        hexadecimal = convertir_a_hexadecimal(numero_decimal)
        print("\nDecimal:", numero_decimal)
        print("Binario:", binario)
        print("Hexadecimal:", hexadecimal)
        print("---------------------------------------------------")
        print()

    elif opcion_seleccionada == 2:
        # Convierte de binario a decimal y hexadecimal.
        cadena_binaria = input("Ingresa un número binario: ")
        decimal = convertir_a_decimal_desde_binario(cadena_binaria)
        hexadecimal = convertir_a_hexadecimal_desde_binario(cadena_binaria)
        print("Binario:", cadena_binaria)
        print("Decimal:", decimal)
        print("Hexadecimal:", hexadecimal)
        print("---------------------------------------------------")
        print()

    elif opcion_seleccionada == 3:
        # Convierte de hexadecimal a decimal y binario.
        cadena_hexadecimal = input("Ingresa un número hexadecimal: ")
        decimal = convertir_a_decimal_desde_hexadecimal(cadena_hexadecimal)
        binario = convertir_a_binario_desde_hexadecimal(cadena_hexadecimal)
        print("Hexadecimal:", cadena_hexadecimal)
        print("Decimal:", decimal)
        print("Binario:", binario)
        print("---------------------------------------------------")
        print()

    else:
        # Si la opción no es válida.
        print("Opción no válida. Por favor, elige una opción entre 0 y 3.")
        print("---------------------------------------------------")
        print()

