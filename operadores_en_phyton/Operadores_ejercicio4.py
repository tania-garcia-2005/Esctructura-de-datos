#***************************************
#****   Tania Garcia Flores.      ******
#****   26 de octubre de 2024.    ******
#***************************************


'''''
Descripción:
Este programa determinará True o False de acuerdo a la expresión (exp1 O exp2) Y (exp3 O exp4).
'''

print()
print("******Expresion booleana (exp1 O exp2) Y (exp3 O exp4)******")#Título.
print()


Valor1=input("Ingrese si/no: ")#Solicita al usuario ingresar en el primer valor booleano si o no.
Valor2=input("Ingrese si/no: ")#Solicita al usuario ingresar en el segundo valor booleano si o no.
Valor3=input("Ingrese si/no: ")#Solicita al usuario ingresar en el tercer valor booleano si o no.
Valor4=input("Ingrese si/no: ")#Solicita al usuario ingresar en el cuarto valor booleano si o no.

Valor_1=Valor1.lower()=="si"#Si el usuario ingresa si aparecera True y en caso contrario aparecera False.
Valor_2=Valor2.lower()=="si"#Si el usuario ingresa si aparecera True y en caso contrario aparecera False.
Valor_3=Valor3.lower()=="si"#Si el usuario ingresa si aparecera True y en caso contrario aparecera False.
Valor_4=Valor1.lower()=="si"#Si el usuario ingresa si aparecera True y en caso contrario aparecera False.


Variable1=Valor_1 or Valor_2#Guarde en una nueva variable el resultado de las 2 variables que son valor 1 y valor 2.
Variable2=Valor_3 or Valor_4#Guarde en una nueva variable el resultado de las 2 variables que son valor 3 y valor 4.

print(f"EL resultado es : {Variable1 and Variable2}")#Imprime el resultado final de todas las comperaciones booleanas.