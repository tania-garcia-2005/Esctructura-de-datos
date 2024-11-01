#***************************************
#****   Tania Garcia Flores.      ******
#****   31 de octubre de 2024.    ******
#***************************************


print()
print("******Lic   informatica******")
print()

numero = int(input("Ingresa el número final de la cuenta: "))

contador = 1
# Recorre los números del 1 hasta el número final de la cuenta.
while contador <= numero:
    # Verificar si es múltiplo de 3 y 5
    if (contador % 3 == 0) and (contador % 5 == 0):
        contador += 1
        print("Licenciatura en Informática", end= " ")
        print()
        # Hace las sustituciones correspondientes por la frase.
    # Verificar si es múltiplo de 3
    elif contador % 3 == 0:
        contador += 1
        print("Licenciatura,",end = "")
    # Verificar si es múltiplo de 5
    elif contador % 5 == 0:
        contador += 1
        print("Informática,",end = "")

    else:
        print(contador,",",end = "")
        contador += 1

