print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.        🍓🍓🍓")
print("🍓🍓Fecha: 24 de Noviembre de 2024     🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print()
print("-----------------------------------------------------------------------------------------------------------------------------------------")
'''''
Descripción:Este programa almacena diversos puntos como coordenadas y permite obtener la ecuación de la recta entre dos de los puntos.

'''

#Definición de mi menú.
def menu():
    print("¸.·✩·.¸¸.·¯⍣✩ Rectas a partir de puntos (coordenadas) en el plano cartesiano ✩⍣¯·.¸¸.·✩·.¸")
    print("1) Ver coordenadas.")
    print("2) Agregar coordenada.")
    print("3) Calcular pendiente y ecuación de la recta.")
    print("4) Eliminar coordenada.")
    print("0) Salir.")
    return input("Elige una opción: ")

#Permite ver las cordenadas ejecutando la opción 1.

def ver_coordenadas(coordenadas):
    if coordenadas:
        print("Coordenadas almacenadas:")
        for i in range(len(coordenadas)):
            print(f"{i + 1}) {coordenadas[i]}")
    else:
        print("No hay coordenadas almacenadas.")

#Funcion para agragar una cordenada por el suario ejecutando la opción 2.
def agregar_coordenada(coordenadas):
    x = float(input("Ingresa la coordenada x: "))
    y = float(input("Ingresa la coordenada y: "))
    coordenadas.append((x, y))
    print(f"Coordenada ({x}, {y}) agregada.")

# Función para calcular  pendiente y ecuación de la recta ejecutando la opción 3.
def calcular_recta(coordenadas):
    if len(coordenadas) < 2:
        print("Necesitas al menos dos coordenadas.")
        return

    ver_coordenadas(coordenadas)
    p1 = int(input("Elige el número del primer punto: ")) - 1
    p2 = int(input("Elige el número del segundo punto: ")) - 1

    x1, y1 = coordenadas[p1]
    x2, y2 = coordenadas[p2]

    if x1 == x2:
        print("Pendiente infinita (recta vertical).")
    else:
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        print(f"Pendiente: {m}")
        print(f"Ecuación: y = {m}x + {b}")

#Función para eliminar la cordenada que desee el usuario  ejecutando la opción 4.
def eliminar_coordenada(coordenadas):
    if coordenadas:
        ver_coordenadas(coordenadas)
        idx = int(input("Elige el número de la coordenada a eliminar: ")) - 1
        eliminada = coordenadas.pop(idx)
        print(f"Coordenada {eliminada} eliminada.")
    else:
        print("No hay coordenadas para eliminar.")

coordenadas = []
opcion = ""#Define una opción para que el bucle no sea infinito.

#Al momento en el que el usuario presiona la opción 0 el programa termina y sale.
while opcion != "0":
    opcion = menu()

    if opcion == "1":
        ver_coordenadas(coordenadas)
    elif opcion == "2":
        agregar_coordenada(coordenadas)
    elif opcion == "3":
        calcular_recta(coordenadas)
    elif opcion == "4":
        eliminar_coordenada(coordenadas)
    elif opcion == "0":
        print("Usted ha salido del programa exitosamente.")
    else:
        print("La opción es inválida.")
