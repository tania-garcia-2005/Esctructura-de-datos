#2 expresiones que me digan si/no
#expresion1=si/no
#expresion1=si/no


cadena_1=input("ingrese si/no: ")
cadena_2=input("ingrese si/no: ")
print(f" La expresion uno es {cadena_1}")  #cadena_2= bool(cadena_2)
cadena_1 = cadena_1.lower() == "si"
print(f" La expresion dos es {cadena_2}")
cadena_2 = cadena_2.lower() == "si"
print(f"¿ambos fueron si? {cadena_1 and cadena_2}")
print(f"¿ambos fueron si? {cadena_1 or cadena_2}")
print(f"¿ambos fueron si? {not cadena_2}")
print(f"¿ambos fueron si? {not cadena_1}")


