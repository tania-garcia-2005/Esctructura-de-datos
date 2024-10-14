'''
#Tania Garcia Flores
#14 octubre de 2024.
Descripción:
Conversión de tipos de datos (casting) en Python.
'''
# Notas
'''
La conversión de tipos de datos implica manipular datos que no están en el tipo de dato requerido. Ejemplos:
de cadena a entero, de cadena a número flotante, y viceversa.
'''

# *****   Conversión de cadena a entero     *****
var_cadena = "951"
var_int = int(var_cadena)

# Utiliza la letra "f" antes de las comillas para indicar que la cadena será formateada.
# Esto significa que puedes incluir variables y expresiones dentro de las llaves {}
# y su valor será insertado en el texto final.
print("Conversión de cadena a entero.")
print(f"Número como cadena: {var_cadena}.")
print(f"Número como int más uno: {var_int + 1}.")


# *****   Conversión de cadena a flotante     *****
var_cadena = "8.88"
var_float = float(var_cadena)
print()
print("Conversión de cadena a flotante.")
print(f"Número como cadena: {var_cadena}.")
print(f"Número como float más cero punto uno: {var_float + 0.1}.")


# *****   Conversión de número a cadena     *****
var_int = 123
var_float = 123.321
print()
print("Conversión de número a cadena.")
print(f"Los números {var_int} y {var_float} se convierten a cadena utilizando str(var_int): {str(var_cadena)}, y "
      f"str(var_float): {str(var_float)}.")


# *****   Conversión a booleano     *****
# Si el valor es 0, cadena vacía o None, la función bool regresa un valor de False. En caso contrario, regresa True.
print()
print("Conversión a booleanos.")

var_int = 0
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")
var_int = -30
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")

var_float = 0.0
es_verdadero = bool(var_float)
print(f"¿El valor de {var_float} es verdadero? {es_verdadero}.")
var_float = 0.01
es_verdadero = bool(var_float)
print(f"¿El valor de {var_float} es verdadero? {es_verdadero}.")

var_cadena = ""
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")
var_cadena = None
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")
var_cadena = " "
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")