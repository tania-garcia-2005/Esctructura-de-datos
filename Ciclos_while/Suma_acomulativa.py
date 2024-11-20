
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
print("🍓🍓   Tania García Flores.   🍓🍓🍓🍓🍓")
print("🍓🍓                          🍓🍓🍓🍓🍓")
print("🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")

'''''
Descripción:Este programa calcula la suma acumulativa, aquí el usuario ingresa el número final en el que realiza lo siguiente---> 
Ejemplo:

Número final ingresado por el usuario:6
lo que se realiza es:1+2+3+4+5+6=21.

'''

###################################################################
print("-----------------------------------------------------------------")
print("****** ★彡『 ℙℝ𝕆𝔾ℝ𝔸𝕄𝔸 ℚ𝕌𝔼 ℂ𝔸𝕃ℂ𝕌𝕃𝔸 𝕃𝔸 𝕊𝕌𝕄𝔸 𝔸ℂ𝕌𝕄𝕌𝕃𝔸𝕋𝕀𝕍𝔸 』彡★ ******")
print("-----------------------------------------------------------------")
print()
print()

numero = int(input("Ingrese el número final de su suma: "))#número de paro.
print()
#asignación de variables.
suma = 0
ayuda = 0
#condición.
while ayuda <= numero:
    suma += ayuda
    ayuda += 1
#imprime el resultado de la suma acomulativa.
print("-----------------------------------------")
print(f"La suma de 0 hasta {numero} es: {suma} ")
print("-----------------------------------------")