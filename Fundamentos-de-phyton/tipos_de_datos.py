#Tania Garcia Flores
#25 de Agosto de 2005.
'''''
Descripción:
Usos de los tipos básico de datos en Python.
'''

# Notas:
"""
En Python, no se requiere indicar el tipo de la variable en su declaración.
Los valores básicos que pueden almacenar las variables son:
- Int
- Float
- String (str)
- Boolean. True o False (con inicial mayúscula).
- None. Tipo especial que representa una ausencia de valor.
"""

# Ejemplos de tipos de datos.

# Número entero
mi_variable_entera = -100
print("Tipo de dato entero:",mi_variable_entera)

# Número decimal
mi_variable_decimal = 12.12
print("Tipo de dato decimal:", mi_variable_decimal)

# Cadena de texto
mi_variable_texto_nombre = "Tania"
mi_variable_texto_apellido = 'Garcia'
print("Cadena de texto:", mi_variable_texto_nombre, mi_variable_texto_apellido)

# Booleno
mi_variable_booleana = True
print('Tipo booleano:', mi_variable_booleana)

# None
mi_variable_none = None
print("Tipo none:",mi_variable_none)

# Uso de constantes.
'''
En Python, a diferencia de otros lenguajes de programación, no existe un tipo específico para definir constantes.
Se utiliza una convención de colocar las variables en mayúsculas y no modificarlas.
'''
VARIABLE_CONSTANTE = 3.1416
print("Ejemplo de convención de una constante:", VARIABLE_CONSTANTE)