#Tania Garcia Flores.
#23 de Octubre del 2024.

'''''
Descripción:
Pide la edad y determina a que grupo pertenece dependiendo de la edad que ingrese.
'''


#elif evalua una condicion
#programa que calcula el grupo de edad al que pertenece
#14 niños y adolecentes
#15 y 25 jovenes
#26 y 45 Adultos jovenes
#46 y 60 Adultos maduros
#60 Adultos mayores


edad=input("ingrese su edad: ")
edad1=int(edad)
if edad1<=14:
    print("Usted pertenece al grupo de niños y adolecentes")
elif edad1>=15 and edad1<=25:
    print(" Usted pertenece al grupo de jovenes :)")
elif edad1>=26 and edad1<=45:
    print("Usted pertenece al grupo de Adultos jovenes")
elif edad1>=46 and edad1<=60:
    print("Usted pertenece al grupo de Adultos maduros")
else:
    print("Usted pertenece al grupo de Adultos mayores")
