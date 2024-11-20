print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.   🍓🍓🍓🍓🍓")
print("🍓🍓                          🍓🍓🍓🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")

'''''
Descripción:Este programa calcula la suma acumulativa, aquí el usuario ingresa el número inicial y el número final ---> 
Ejemplo:
Número inicial ingresado por el usuario:4
Número final ingresado por el usuario:9
lo que se realiza es:4+5+6+7+8+9=39.

'''

###################################################################
print("-----------------------------------------------------------------")
print("****** ★彡『 ℙℝ𝕆𝔾ℝ𝔸𝕄𝔸 ℚ𝕌𝔼 ℂ𝔸𝕃ℂ𝕌𝕃𝔸 𝕃𝔸 𝕊𝕌𝕄𝔸 𝔸ℂ𝕌𝕄𝕌𝕃𝔸𝕋𝕀𝕍𝔸 』彡★ ******")
print("-----------------------------------------------------------------")
print()
print()



numero_inicial = int(input("Ingrese su número inicial: "))#número con el que  inicia la suma acumulativa.
print("-----------------------------------------------------------------")
numero_final = int(input("Ingrese su número final: "))#Número en el que termina la suma acumulativa.
print("-----------------------------------------------------------------")

print(f"La suma de {numero_inicial} hasta {numero_final} es: ")#impime el número inicial y final que el usuario ingreso.
suma = 0#contador.
#condición.
while numero_inicial <= numero_final:
    #operaciónes.
    suma += numero_inicial
    numero_inicial += 1
print(suma)#total.