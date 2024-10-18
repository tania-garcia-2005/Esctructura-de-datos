#Tania Garcia Flores
#18 de Octubre 2024
"""
Entrada_conversiones_ejercicio.py

Escribe un programa de nombre Entrada_conversiones_ejercicio.py que realice lo siguiente:

a) Pida los datos de los profesores utilizando nombres de variables adecuadas, la función input y el casting:

Nombre (cadena).
No. de cubículo (int).
Horas de que imparte clase a la semana (float con 3 decimales).
¿Tiene más de 5 años en la unsij? (booleno).
b) Muestre los datos en consola de forma adecuada.

Nota: Asuma que el usuario siempre va a ingresar números cuando se requiera.
"""

cadena=input("Ingrese su Nonbre: ")
cubo=input("Ingrese el numero de su cubiculo: ")
horas=input("ingreses el total de horas que imparte clase a la semana: ")
horas1=float(horas)

pregunta= input("¿tiene mas de 5 años en la UBSIJ?(si/no: ")

pregunta=pregunta.lower()=="si"
print(f"su nombre es: {cadena}")
print(f"su cubo es: {cubo}")
print(f"sus horas son: {horas1}")
print(f"tiene mas de 5 años en la UBSIJ: {pregunta}")
