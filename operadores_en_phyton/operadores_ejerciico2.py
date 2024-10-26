#***************************************
#****   Tania Garcia Flores.      ******
#****   17 de octubre de 2024.    ******
#***************************************


# Operadores lódicos.
'''''
Descripción:
Este programa determinará si el usuario pertenece a la comunidad de la Unsij.
'''

print()
print("******Comunidad de la Unsij******")#Título.
print()

#¿Es profesor de la UNSIJ?
#¿Es estudiante de la UNSIJ?
#¿Forma parte de la comunidad de la UNSIJ?  true/false



Profesor=input("Es profesor de ela UNSIJ? si/no: ")
Alumno=input("Es alumno de ela UNSIJ? si/no: ")

Profesor=Profesor.lower()=="si"#En caso de que el usuario ingrese un "mo"aparecera en pantalla false.
Alumno=Alumno.lower()=="si"#En caso de que el usuario ingrese un "mo"aparecera en pantalla false.
print(f"Forma parte de la comunidad UNSIJ? {Profesor or Alumno}")#Imprime True o Flase dependiendo de la respuesta que ingrese el usuario.