#Tania Garcia Flores
#15 de octubre de 2024.
#Se utiliza para comparar dos valores

#tiene que imprimir el primer valor de el numero que en este caso seria el 87

numero1 = input("Introduce un número : ")
numero2 = input("Introduce otro número : ")


num1 = float(numero1)
num2 = float(numero2)

#{numero1:2f}
print(f"¿El primer numero {num1:.2f} es ,mayor a {num2:.2f}?: {numero1>numero2}") #se pone {num1:.2f} y {num2:.2f} para que a la hora de imprimir aparesca el valor y despues indique si es verdadero o falso (tru or false)
print(f"¿El primer numero {num1:.2f}  es ,mayor igual a {num2:.2f}?:{numero1>=numero2}")
print(f"¿El numero {num1:.2f} es igual a {num2:.2f}?: {numero1==numero2}")
print(f"¿El primer numero {num1:.2f} es ,menor a {num2:.2f}?: {numero1<numero2}")
print(f"¿El primer numero {num1:.2f} es ,menor igual a {num2:.2f}?: {numero1<=numero2}")
print(f"¿El primer numero {num1:.2f} es diferente del numero {num2:.2f}?: {numero1!=numero2}")







