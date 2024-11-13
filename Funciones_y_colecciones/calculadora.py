print("****************************************")
print("****   Tania Garcia Flores.        *****")
print("****   11 de Noviembre de 2024.    *****")
print("****************************************")

'''''
Descripción:Realiza la calculadora con las llamadas de  funciones

'''

print()
print("******  Programa que realiza la calculadora(con ciclos) ******")
print()

def menu ():

    print("1)suma")
    print("2)resta")
    print("3)multipcicacion")
    print("4)division")
    print("5)division entera")
    print("6)modulo")
    print("7)exponenciación")
    print()
    seleccion=int(input("ingrese su opcion"))
    return seleccion
#
def calculadora(opcion,numero1,numero2):

    if opcion==1:
        resultado=numero1+numero2
    elif opcion==2:
        resultado=numero1-numero2
    elif opcion==3:
        resultado = numero1 *numero2
    elif opcion==4:
        resultado=numero1/numero2
    elif opcion == 5:
        resultado = numero1 // numero2
    elif opcion == 6:
        resultado = numero1 % numero2
    elif opcion == 7:
        resultado = numero1 ** numero2
    return resultado


numero1=float(input("Ingrese su primer numero:"))
numero2=float(input("Ingrese su segundo numero:"))
opcion=menu()
resultado2=calculadora(opcion,numero1,numero2)
print(f"Su resultado es:{calculadora(opcion,numero1,numero2)}")





