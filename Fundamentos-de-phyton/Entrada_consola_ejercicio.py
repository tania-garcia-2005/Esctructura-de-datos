#Tania Garcia Flores
#18 de Octubre 2024

''''
ENTRADA CONSOLA EJERCICIO

a) Pida 2 números decimales por consola al usuario utilizando la función input.

b) Muestre los resultados de las operaciones básicas con esos números: suma, resta, multiplicación y división.

Nota: Asuma que el usuario siempre va a ingresar números y que el segundo número es diferente de cero.
'''
#a)solicita 2 numeros al usuario
v_numero = input("Introduce un número decimal: ")
v_numero2 = input("Introduce otro número decimal: ")
#convierte los numeros

numero1=float(v_numero)
numero2=float(v_numero2)

#b) Muestre los resultados de las operaciones básicas con esos números: suma, resta, multiplicación y división.
print("*****SUNA*****")#realiza la suma de 2 numeros
suma=numero1+numero2
print(f"El resultado de la suma es: {suma:.2f}")
print()


print("*****RESTA*****")#realiza la resta de 2 numeros
resta=numero1-numero2
print(f"El resultado de la resta es: {resta:.2f}")
print()


print("*****MULTIPLICACION*****")#realiza la multiplicacion de 2 numeros
multiplicacion=numero1*numero2
print(f"El resultado de la multiplicacion es: {multiplicacion:.2f}")
print()


print("*****DIVISION*****")#realiza la dividsiom de 2 numeros
division=numero1/numero2
print(f"El resultado de la division es: {division:.2f}")
print()
