#***************************************
#****   Tania Garcia Flores.      ******
#****   28 de octubre de 2024.    ******
#***************************************


print()
print("******Lic   informatica******")
print()

numero = int(input("Ingresa el número final de la cuenta: "))

contador = 1
# Recorrer los números del 1 hasta el número ingresado
while contador <= numero:
    # Verificar si es múltiplo de 3 y 5
    if (contador % 3 == 0) and (contador % 5 == 0):
        contador += 1
        print("Licenciatura en Informática", end= " ")
        print()
        # Sustituir por la frase
    # Verificar si es múltiplo de 3
    elif contador % 3 == 0:
        contador += 1
        print("Licenciatura,",end = "")  # Sustituir por la palabra
    # Verificar si es múltiplo de 5
    elif contador % 5 == 0:
        contador += 1
        print("Informática,",end = "")  # Sustituir por la palabra

    else:
        print(contador,",",end = "")  # Imprimir el número
        contador += 1

