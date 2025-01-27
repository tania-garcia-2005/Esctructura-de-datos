"""
Descripción:
En los archivos Saludar_modulo.py y Saludar_main.py se ejemplifica el uso de los módulos y de la
sentencia if __name__ == "__main__"

Los módulos son una herramienta esencial en Python para organizar código y promover la reutilización.
Al comprender cómo crear e importar módulos, se podrá escribir programas más eficientes, mantenibles y colaborativos.

Por otro lado, la sentencia if __name__ == "__main__": es una construcción que permite controlar si un archivo
se está ejecutando como un script principal o si está siendo importado como un módulo en otro script.
"""

# Se importa la función saludar() del módulo Saludar_modulo.py
from Saludar_modulo import saludar

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
# __name__ es una variable especial que Python asigna a cada módulo.
# Si el módulo se está ejecutando directamente, __name__ será igual a "__main__".
# Si el módulo está siendo importado en otro script, __name__ será igual al nombre del módulo.
# La condición if name == "main": verifica si el módulo se está ejecutando como el programa principal.
# Si es así, el código dentro de este bloque se ejecutará.
if __name__ == '__main__':
    nombre = input("Ingresa la persona a saludar: ")
    saludar(nombre)

# Nota:
# Probar ambos archivos con y sin la condición if __name__ == '__main__'
