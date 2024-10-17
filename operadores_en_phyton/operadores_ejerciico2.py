#Tania Garcia Flores
#15 de octubre de 2024.
#¿Es profesor de la UNSIJ?
#¿Es estudiante de la UNSIJ?
#¿Forma parte de la comunidad de la UNSIJ?  true/false



profesor=input("Es profesor de ela UNSIJ? si/no: ")
alumno=input("Es alumno de ela UNSIJ? si/no: ")

profesor=profesor.lower()=="si"
alumno=alumno.lower()=="si"
print(f"Forma parte de la comunidad UNSIJ? {profesor or alumno}")