print("****************************************")
print("****   Tania Garcia Flores.        *****")
print("****   19 de Noviembre de 2024.    *****")
print("****************************************")

'''''
Descripción:. 

'''

print("------------------------------------------------------------------------")
print()
print("****** serie de pi******")
print()

#serie de pi leibniz

pi_serie=(4,-4/3,4/5,-4/7,4/9,-4/11,4/13,-4/15,4/17,-4/19,4/21,-4/23)
print(f"El valor de pi considerando 3 elementos:{sum (pi_serie[0:2]):.4f}")
pi_serie=(4,-4/3,4/5,-4/7,4/9,-4/11,4/13,-4/15,4/17,-4/19,4/21,-4/23)
print(f"El valor de pi considerando 5 elementos:{sum (pi_serie[0:4]):.4f}")
pi_serie=(4,-4/3,4/5,-4/7,4/9,-4/11,4/13,-4/15,4/17,-4/19,4/21,-4/23)
print(f"El valor de pi considerando 8 elementos:{sum (pi_serie[0:7]):.4f}")
pi_serie=(4,-4/3,4/5,-4/7,4/9,-4/11,4/13,-4/15,4/17,-4/19,4/21,-4/23)
print(f"El valor de pi considerando 10 elementos:{sum (pi_serie[0:9]):.4f}")
pi_serie=(4,-4/3,4/5,-4/7,4/9,-4/11,4/13,-4/15,4/17,-4/19,4/21,-4/23)
print(f"El valor de pi considerando todos los elementos:{sum (pi_serie):.4f}")
print("------------------------------------------------------------------------")
print()
print("****** Ejemplo de cordenadas ******")
print()

punto1=(1,0)
punto2=(5,3)
print()
print(f"cordenadas en tuplas:{punto1}{punto2}")
#Desempaquetado de tuplas
x1,y1=punto1
x2,y2=punto2

pendiente=(y2-y1)/(x2-x1)
b=y1-pendiente*x1
print(f"La expresion de la recta es: y={pendiente}x{b}")
print("------------------------------------------------------------------------")



