print("****************************************")
print("****   Tania Garcia Flores.        *****")
print("****   11 de Noviembre de 2024.    *****")
print("****************************************")

'''''
Descripción:Realiza la 

'''

print()
print("****** Lista alumnos ******")
print()

#mutable: Su significado es que:puede crecer o reduirse.
#pila.Queve
#lifo:el ultimo en entras es el primero en salir
#para añadir un elemento a una lista se escribe el nombre un punto y despues la palabra reservada append
#ejemplo:   alumnos.append("Hector")

alumnos=[]
alumnos.append("Hector")
alumnos.append("Tania")
alumnos.append("Addi")
alumnos.append("Alberto")
alumnos.append("Juan")
alumnos.insert(1,"Tania")
alumnos.pop(2)
del alumnos[2]
print(alumnos)
for alumno in alumnos:

    print(alumno,end=" ")

#.remove("Hector")#eliminr por valor
#.pop(2)    #elimina por subindice
# del alumnos[2] Hcetor #elimina por indice
#para insertar valores en un indice especifico
#si solo quierpo mostrar uno el nombre de la variable corchetes el numero




