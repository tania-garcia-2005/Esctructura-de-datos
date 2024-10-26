#***************************************
#****   Tania Garcia Flores.      ******
#****   26 de octubre de 2024.    ******
#***************************************


'''''
Descripción:
Este programa determinará si un usuario se autentifica correctamente con su usuario y contraseña.
'''

print()
print("******Sistema de Autentificación******")#Título.
print()

USUARIO= "Tania.Garcia"#Se declaro internamente el usuario  que se debe ingresar para que sea correcto.(en Phyton no exísten constantes pero si se pueden poner como mayúsculas)
CONTRASEÑA="1234"#Se declaro internamente la contraseña  que se debe ingresar para que sea correcta.
print()
print("******Sistema de Autentificación******")#Título.
print()

Usuario2=input("Ingrese un usuario: ")#Pide que el usuario ingrese su usuario.
Contraseña2=input("Ingrese su contraseña: ")#Pide que el usuario ingrese su contraseña.

print(f"El acceso fue correcto?: {Usuario2==USUARIO and Contraseña2==CONTRASEÑA }")#Con ayuda de el Operador relacional "and" verifica si el usuario y contraseña son correctos e imprime true,en caso contrario imprime False.