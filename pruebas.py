'''
Nombre:
Fecha:
Descripción:
Entrada de datos por consola para interacturar con el usuario con valores dinámicos.
'''

# Comentar sobre la función input.
numero1_cadena = input("Introduce un número decimal: ")
numero2_cadena = input("Introduce otro número decimal: ")
resultado_cadena = numero1_cadena + numero2_cadena # Verificar qué es lo que realiza esta instrucción (ver el print).
print()
print(" ****  Recibir número sin un casting de varibles  ****")
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}")
#el resultADO ES UNA CONCATENACION T NO LA SUMA

# Comentar por qué se realiza el casting de variables.
numero1_float = float(numero1_cadena)
numero2_float = float(numero2_cadena)
resultado_float = numero1_float + numero2_float # Verificar qué es lo que realiza de esta manera y compáralo.
print()
print(" ****  Casting de varibles  ****")
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")
#FUNCIONES ANIDADAS
EJERCICIO



'''
Nombre:
Fecha:
Descripción:
Conversión de cadenas a int, float y boolean mediante la interacción con consola.
'''

# Comentar sobre las funciones anidadas.
print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ")
semestre = int(input("Ingresa el no. de semestre: "))
promedio = float(input("Ingresa el promedio: "))
es_mujer = input("¿Es mujer (Si/No)?: ")
# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si"

# Se imprimen los datos del alumno.
# Comentar  qué es lo que realiza {promedio:.2f} probando con números diferentes.
print()
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")

Escribe un programa de nombre Entrada_conversiones_ejercicio.py que realice lo siguiente:

a) Pida los datos de los profesores utilizando nombres de variables adecuadas, la función input y el casting:

Nombre (cadena).
No. de cubículo (int).
Horas de que imparte clase a la semana (float con 3 decimales).
¿Tiene más de 5 años en la unsij? (booleno).
b) Muestre los datos en consola de forma adecuada.

Nota: Asuma que el usuario siempre va a ingresar números cuando se requiera.

