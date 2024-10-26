#***************************************
#****   Tania Garcia Flores.      ******
#****   17 de octubre de 2024.    ******
#***************************************


# Operadores lódicos.
'''''
Descripción:
Este programa determinará si el usuario aplica para una bonificación.
'''

print()
print("******Sistema de Bonificación******")#Título.
print()

Cantidad=input("¿Realizó compras mayores a $5000.00?. (Favor de ingresar  su cantidad en decimales): ")#Pregunta al usuario si realiza compras mayores a $5000 y que ingrese la cantidad en decimales.
Cadena= input("¿Compras a MSI?(si/no: ")#Pide al usuario que ingrese si realiza sus compras a meses sin intereses y en caso contrario debe ingresar no.

Total=float(Cantidad)
Variable_Bool = bool(Cantidad)
Cadena=Cadena.lower()=="si"#En caso de que el usuario ingrese un "mo"aparecera en pantalla false.
print(f"¿Aplica bonificación?{Variable_Bool>5000 and Cadena}")#Imprime False o True,dependiendo de la respuesta de el usuario.


