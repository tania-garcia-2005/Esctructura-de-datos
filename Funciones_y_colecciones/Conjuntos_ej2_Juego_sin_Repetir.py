print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")#Portada.
print("🍓🍓   Tania García Flores.   🍓🍓🍓🍓🍓")
print("🍓🍓                          🍓🍓🍓🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
#Nombre de mi programa.
print("----------------------------------------------------------------------------------")
print("****** ★彡🎀JUEGO SIN REPETIR🎀』彡★ ******")
print("----------------------------------------------------------------------------------")
print()

#Imprimi mis intrucciones para que el usuario sepa cómo jugar.
print("INSTRUCCIONES:")
print()
print("--------------------------------------------------------------------")
print(" Este es un juego que se puede jugar de manera grupal")
print(" en donde el objetivo es decir palabras de un tema en específico")
print(" y los jugadores deben tratar de no repetir la misma palabra.")
print("--------------------------------------------------------------------")
print()

#Definición de mi conjunto.
juego = set()
tema = input("Ingrese el tema del juego: ")#tema que el usuario desee.

# Esta variable controla si el juego sigue o no,el número "1" significa que el juego está ejecutandose..
continuar = 1
#Mientras no se repitan las palabras el juego continua.
while continuar:
    np = len(juego) + 1#Controla el turno  calculando el número de palabras ingresadas por el usuario más una para mostrar el turno.
    palabra = input(f"Ingrese la palabra {np} del tema '{tema}': ").strip().lower()#Se pide al usuario que ingrese una palabra que este relacionada con el tema.
#Revisión de que la palabra no se haya repetido antes.
    for revisar in juego:
        if revisar == palabra:
            continuar = 0#Fin del juego.
    else:
        juego.add(palabra)#Si la palabra aún no se ha repetido,se agrega al conjunto.

print(f"El juego  se ha terminado. Se han dicho {np} palabras diferentes ")# Muestra que el juego ha terminado y cuántas palabras diferentes se dijeron.
print(f"Las palabras del tema {tema} fueron: {juego}")#Muestra todas las palabras relacionadas con el tema.