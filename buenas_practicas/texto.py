import time

# Códigos ANSI que cambian el color de mis letras.
MORADO = "\033[38;5;128m"  # Morado claro
AZUL = "\033[34m"  # Azul
AMARILLO = "\033[33m"  # Amarillo
VERDE = "\033[32m"  # Verde
RESET = "\033[0m"  # esto hace que se vuelva al color inicial.
def mostrar_mensaje(mensaje, retraso=0.1):#aquí en retraso pongo la velocidad que quiero, y entre más ceros le ponga será más rapido.
    colores = [MORADO, AZUL, AMARILLO, VERDE]  #Colores que ocupare.
    for i, caracter in enumerate(mensaje):
        color = colores[i % len(colores)]  # Cicla entre los colores
        print(color + caracter, end='', flush=True)  # Aplica el color a las letras.
        time.sleep(retraso)
    print(RESET)  #Esto vuelve al color original.

mensaje = """Me quieren agitar,
Me incitan a gritar,
Soy como una roca,
Palabras no me tocan,
Adentro hay un volcán,
Que pronto va a estallar,
Yo quiero estar tranquilo."""
mostrar_mensaje(mensaje)
