#Declaramos las variavles
renta = int(input("Introducir numero"))
#Declaro el tipo impositivo segun la cantidad
#comprobamos a que tramo pertenece
if rent1< 1000:
    imp = 5
elif rent1< 2000:
    imp = 15
elif rent1< 3500:
    imp = 20
elif rent1< 6000:
    imp = 30
#imprimimos en pantala el tipo impositivo
print("El tipo impositivo es", imp, "%")
