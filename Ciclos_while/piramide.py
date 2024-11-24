print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.   🍓🍓🍓🍓🍓")
print("🍓🍓7 de noviembre  de 2024   🍓🍓🍓🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")

'''''
Descripción:Este programa realiza una piramide utilizando el ciclo for en phyton. 
.

'''

###################################################################
print("----------------------------------------------------------------------------------")
print("****** ★彡🎀『 【p】【i】【r】【a】【m】【i】【d】【e】🎀』彡★ ******")
print("----------------------------------------------------------------------------------")
print()
print()

#letrero.
fila = int(input("🛕Ingrese el número de filas que desee para su piramide🛕: "))
print("----------------------------------------------------------------------------------")
#Asigna la fila=filas ingresadas por el usuario en una nueva variable.
fila1 = fila
contador = fila
#Realiza el ciclo for para la impresion de un triangulo.
'''
* 
*  * 
'''

print("Primer triángulo")
for i in range(1, fila1 + 1) :
    asteriscos1 = " * " * i
    print(f" {asteriscos1}")


print()
print("----------------------------------------------------------------------------------")
print("Segundo triángulo")
#Realiza el ciclo for para la impresion de un triangulo.
'''
*  * 
* 
'''
fila1 = fila
contador = fila
for x in range(1, fila + 1) :
    asteriscos2 = " * " * fila1
    fila1 = fila1 - 1
    print(f" {asteriscos2}")
print()
print("----------------------------------------------------------------------------------")




print("Tercer triángulo")
#Realiza el ciclo for para la impresion de un triangulo.
'''
 *

**
'''
fila1 = fila
contador = 0
for z in range(1, fila1 + 1):
    print(" " * (fila1 - z) + "*" * z)
    print()

print("----------------------------------------------------------------------------------")

print("Cuarto triángulo")
#Realiza el ciclo for para la impresion de un triangulo.
'''
 *
***
'''
fila1 = fila
contador = fila1
contador=0

for i in range(1, fila + 1):
    asteriscos="*" * (contador + 1)
    espacio=" " * (fila - i)
    contador+=2##Ejecuta el programa y el espacio(primer asterisco)le va sumando 2 y así sucesivamente basándose en las filas que ingrese el usuario.
    print(f" {espacio}{asteriscos}")