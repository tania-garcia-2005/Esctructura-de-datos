#***************************************
#****   Tania Garcia Flores.      ******
#****   6 de Noviembre de 2024.   ******
#***************************************

'''''
Descripción: Realiza el for e imprime la palabra con espacios de "-"

'''

print()
print("******  Programa que realiza el ciclo for ******")
print()


#Declaraciones
variable=0
contador=0
caracter=0
cadena=input("ingresa una cadena: ")#Solicita una cadena de letras al usuario.

for caracter in cadena:#En phyton esta es la declaración que se debe hacer para implementar un ciclo for.
    contador+=1
    print(caracter, end="-")#Imprime en consola la cadena ingresada por el usuario con espacion sustituidos por un "-"
