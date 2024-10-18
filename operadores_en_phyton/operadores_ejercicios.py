#Tania Garcia Flores
#17 de octubre de 2024.



cantidad=input("¿Compras mayores a $5000.00? por favor ingrese su cantidad en decimales: ")
cadena= input("¿Compras a MSI?(si/no: ")

total=float(cantidad)
variable_bool = bool(cantidad)
cadena=cadena.lower()=="si"
print(f"¿Aplica bonificacion?{variable_bool>5000 and cadena}")


