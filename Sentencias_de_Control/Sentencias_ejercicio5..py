#***************************************
#****   Tania Garcia Flores.      ******
#****   26 de octubre de 2024.    ******
#***************************************

'''''
Descripción:
Este programa determinará el promedio de una materia e indicará si el alumno aprobó o no la materia.
'''

print()
print("******  Programa para calcular el promdeio de una materia  ******")
print()

'''

Si ambas condiciones se cumplen, se imprime el mensaje en consola: "¡Felicidades aprobaste!". En caso contrario, se imprime: "Lo siento,no aprobaste"
Para ello:
a) Solicite al usuario sus tres calificaciones parciales y la calificación del ordinario.
b) Calcule el promedio y determine si aprobó (calificación mínima de 6.0).
d) Muestre el promedio (utilizando un decimal) y el mensaje: "¡Felicidades! Aprobaste.", o el mensaje: "Lo siento, no aprobaste.", según sea el caso.

'''
#solicita ingresar las calificaciones de sus parciales y ordinario.

calificación1=float(input("Ingrese su calificacion del parcial 1: "))
calificación2=float(input("Ingrese su calificacion del parcial 2: "))
calificación3=float(input("Ingrese su calificacion del parcial 3: "))
ordinario=float(input("Ingrese su calificacion de su ordinario: "))


promedio_total=(calificación1 + calificación2 + calificación3)/3 #Calcula el promedio final sumando las primeras 3 calificaiones y las divide entre de 3.
variable=(promedio_total*0.5)+(ordinario*0.5)#El promedio obtenido lo multiplica por 0.5 y le suma la calificacion de el ordinario multiplicado también por 0.5 (se multiplica por 0.5 por que equivale al 50% de la calificaciones la suma de los 3 parciales y el otro 50% equivale al ordinario.
#imprime los mensajes de acuerdo al valor obtenido.
if variable >= 6.0:
    print(f"Su promedio es de: {variable:.1f}")
    print(f"¡Felicidades! Aprobaste.")
else:
    print(f"Su promedio es de: {variable:.1f}")
    print(f"Lo siento, no aprobaste.")
