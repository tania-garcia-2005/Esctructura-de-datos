#***************************************
#****   Tania Garcia Flores.      ******
#****   26 de octubre de 2024.    ******
#***************************************

'''''
Descripción:
Este programa determinará un descuento en compras en "La cona".
'''

print()
print("****** Descuentos por ser miebros de  'La cona' ******")
print()

'''
•	Si tiene membresía, obtiene un 5 % de descuento en todas sus compras.
•	Si tiene la membresía y su compra fue mayor o igual a $ 1000.00, entonces el descuento es del 8 %.
•	Si no tiene la membresía, no obtiene ningún descuento y se invita a ser miembro.
Para ello:
a) Solicite al usuario la cantidad comprada en la tienda.
b) Pregunte al usuario si cuenta con la membresía (Si/No).
c) Utilice la lógica adecuada para determinar el total a pagar.
d) Muestre el descuento y el total a pagar en consola utilizando dos decimales.
'''


Cantidad=float(input("Ingrese su cantidad comprada en la tienda: "))#Letrero.
membresia= input("Cuenta con la membresía?(si/no): ")#Letrero.
membresia=membresia.lower()=="si"
#Realiza las comparaciones correpondientes.
if membresia:
    if Cantidad >= 1000:
        total= Cantidad * 0.08#Aplica el descuento del 8%.
        pagar= Cantidad - total
        print(f"Tu descuento es del 8% {pagar:.2f} ")

    else:
        total = Cantidad * 0.05#Aplica el descuento de 5%.
        pagar = Cantidad - total
        print(f"Tu descuento es del 5% {pagar:.2f} ")

else:
    print("No obtiene ningún descuento,te invitamos  a ser miembro.")#Este mesaje se imrpime si no se cumplen las condiciones anteriores.


