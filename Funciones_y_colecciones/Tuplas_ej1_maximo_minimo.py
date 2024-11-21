print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓Fecha: 21 de Noviembre de 2024     🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")

'''''
Descripción: Este programa muestra el valor máximo y mínimo de una lista de números. En este caso, la tupla se utiliza para devolver los valores máximo y mínimo de la función.
'''

###################################################################################################
def menu ():
#Definicion del menú
    print("1)Ver lista de numeros")
    print("2)Añadir número a la lista")#nombre y cantidad
    print("3)Determinar el valor máximo y mínimo de la lista de números")
    print("0)Salir")

    print()
    opcion = int(input("ingrese su opción:"))

    return opcion


def  añadir_numero(lista_de_numeros):

    print()
###################################################################
print("-------------------------------------------------------------------------------------------")
print("****** 🌸ꗥ～ꗥ🌸  𝐕𝐚𝐥𝐨𝐫 𝐦á𝐱𝐢𝐦𝐨 𝐲 𝐦í𝐧𝐢𝐦𝐨 𝐝𝐞 𝐮𝐧𝐚 𝐥𝐢𝐬𝐭𝐚 𝐝𝐞 𝐧ú𝐦𝐞𝐫𝐨𝐬 𝐝𝐞𝐥 𝐮𝐬𝐮𝐚𝐫𝐢𝐨  🌸ꗥ～ꗥ🌸 ******")
print("-------------------------------------------------------------------------------------------")
print()
print()

lista = []
opcion = None  # None sustituye al -1,para tener una variable opuesta a tu condiicioon del while(no tiene ningun valor)
while opcion!=0:
    opcion = menu()


    if opcion==1:
        print(lista)
        print("----------------------------------------------------")
        print()





