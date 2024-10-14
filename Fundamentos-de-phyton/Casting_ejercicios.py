'''
#Tania Garcia Flores
#14 octubre de 2024.
Descripción:
Conversión de tipos de datos (casting) en Python.
'''
# Notas
'''
# Realiza un programa de nombre Casting ejercicio p que realice lo siguiente.
# a) Convierta los siguientes números en cadenas: 3.14159265, 12, 0.
# b) De los números anteriores, indica su valor booleano
# c) Convierta las siguientes cadenas a números: "10002*1400.02" "0°
# d) De las cadenas anteriores, indica su valor booleano. Nota especificar por qué el resultado de la cadena "O"
'''


# *****   Conversión de número a cadena     *****
var_int = 3.14159265
print()
print("Conversión de número a cadena.")
print(f"Los números {var_int} se convierten a cadena utilizando str(var_int): {str(var_int)}.")
var_int = 0
print()
print("Conversión de número a cadena.")
print(f"Los números {var_int} se convierten a cadena utilizando str(var_int): {str(var_int)}.")
var_int = 12
print()
print("Conversión de número a cadena.")
print(f"Los números {var_int} se convierten a cadena utilizando str(var_int): {str(var_int)}.")

# **   Conversión a booleano     **
# Si el valor es 0, cadena vacía o None, la función bool regresa un valor de False. En caso contrario, regresa True.
print()
print("Conversión a booleanos.")

var_int = 0
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")

print()
print("Conversión a booleanos.")

var_int = 3.14159265
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")
print()
print("Conversión a booleanos.")

var_int = 12
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")


# **   Conversión de cadena a entero     **
var_cadena = "0"
var_int = int(var_cadena)
print("La cadena  a entero es: ", var_cadena)
# **   Conversión de cadena a entero     **
var_cadena = "12"
print("La cadena  a entero es: ", var_cadena)
var_int = int(var_cadena)

# **   Conversión de cadena a entero     **
var_cadena = "3.14159265"
print("La cadena  a entero es: ", var_cadena)
var_int = float(var_cadena)

#insiso d

print()
print("Conversión a booleanos.")

var_cadena = "3.14159265"#sale true por que es una cadena y esta completa
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")
print()
print("Conversión a booleanos.")

var_cadena = "0" #sale true por que es una cadena y no es una cadena vacia,en caso contrario se que fuese una cadena vacia si seria false
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")

print()
print("Conversión a booleanos.")

var_cadena = "12"#es una cadena completa por lo tanto es el resultado true,los casos false salen cuando las cadena son vasias,cuando es cero y cuando es none
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")




