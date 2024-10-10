# Tania Garcia Flores
# 25 de Agosto de 2005
# En este archivo se ejemplifica el uso de variables en Pythonnn
# Notas:
# En Python todo es mas facil .
# Variable - una variable es un nombre que almacena un valor guardado en la memoria temporal

# Toda variable requiere un valor inicial
semestre = 3        # es una variable que apunta a un objeto de tipo int con valor de 3
print(semestre)     # imprime el valor de la variable
semestre = 4        # la variable ya no apunta al objeto anterior, sino a uno nuevo, por lo que se pierde la referencia
print(semestre)

# Se crean varias variables para ejemplificar su uso
nombre = "Patricia Pérez Cruz"  # variable de tipo String
altura = 1.50      # variable de tipo Float
edad = 18         # variable de tipo Int
semestre = 3
# Se imprimen las variables, añadiendo información adicional para comprender lo que se imprime
print("Nombre:", nombre)
print("Semestre:", semestre)
print("Altura: ", altura, "cm.")
print("Edad: ", edad, "años.")

# Se modifican los valores de las variables y se mandan a imprimir
altura = 1.50
edad = 19
semestre = 4

print() #El print ya viene incluido el salto de linea sin necesidad de poner "/n"
print("Valores modificados:")
print("Nombre:", nombre)
print("Semestre:", semestre)
print("Altura: ", altura, "cm.")
print("Edad: ", edad, "años.")

# En Python, las variables son dinámicas, por lo que pueden almacenar otro tipo de dato en cualquier momento
edad = "diecinueve"      # edad antes tenía el valor de 18 (Int)


print()
print("Edad (con otro tipo de dato):", edad)


# Reglas para los nombres de las variables en Python:
# - Utilizar únicamente letras (mayúsculas o minúsculas), números y el guion bajo
# "Esto de arriba es en el momento de declarar una variables"


print()
# - La variable no puede iniciar con números
# - No se pueden utilizar palabras reservadas, ejemplos: if, else, True, class
# - Es sensible a mayúsculas y minúsculas. Por ejemplo, las palabras "Hola", "hola" y "HOLA" son consideradas diferentes.

# Buenas prácticas
# - Utilizar minúsculas para las palabras
# - Separar las palabras con el guion bajo
# - Utilizar nombres descriptivos de acuerdo a su uso. Por ejemplo: edad, en lugar de e.

# Ejemplos correctos y con buenas prácticas
fecha_nacimiento = "25 de agosto del 2005"
clase = "Estructuras de Datos"
horas_estudio = 8
nombre = "Tania"
es_estudiante = True

# Ejemplos incorrectos (líneas comentadas porque marcan error) o de malas prácticas
f = "25 de agosto del 2005"
fechanacimiento = "25 de agosto del 2005"
print()
#class = "Estructuras de Datos"
# 8horas_estudio = 8
Nombre = "t a n i a "
NOMBRE = "TANIA"

# Notar que las variables 'nombre', 'Nombre' y 'NOMBRE', son distintas
print()
print("Las variables son sensibles a mayúsculas y minúsculas:")
print("Variable nombre:", nombre)
print("Variable Nombre:", Nombre)
print("Variable NOMBRE:", NOMBRE)