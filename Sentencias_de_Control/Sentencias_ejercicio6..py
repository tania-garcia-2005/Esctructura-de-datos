#***************************************
#****   Tania Garcia Flores.      ******
#****   26 de octubre de 2024.    ******
#***************************************

'''
Descripción:
Este programa mostrará los detalles del tour turístico Ecoturixtlán de acuerdo a las siguientes tarifas:
• Precio de un adulto: $ 200.00
• Precio de un niño: $ 100.00
Además, si la visita son los lunes, martes y jueves, se tiene un descuento del 10 %.
'''

print()
print("****** Tour turístico Ecoturixtlán  ******")
print()

# Definición de las constantes para los precios.
precio_adulto = 200.00
precio_niño = 100.00
descuento_días = {"lunes", "martes", "jueves"}
tasa_descuento = 0.10

# Solicita el nombre de la persona a cargo
persona = input("Ingrese el nombre de la persona a cargo: ")

# Solicitar el número de adultos y niños.
adultos = int(input("Ingrese el número de adultos: "))
niños = int(input("Ingrese el número de niños: "))

# Día de la semana
dia = input("Ingrese el día de la semana: ")

# Aquí se calcula el costo total.
costo_total = (adultos * precio_adulto) + (niños * precio_niño)

# Aplica el descuento si es necesario.
if dia ==descuento_días:
    monto_descuento = costo_total * tasa_descuento
    costo_total -= monto_descuento
    descuentos = " (Se aplicó el 10% de descuento)"
else:
    descuentof = ""

print()
print(f"Detalles del cliente: {persona}")
print(f"Día de la visita: {dia}")
print(f"Costo total: ${costo_total:.2f}{descuentof}")



