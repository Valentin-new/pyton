num1 = int(input("introduce el primer numero : "))
num2 = int(input("introduce el segundo numero : "))
print("1-suma")
print("2-resta")
print("3-multiplicacion")
print("4-division")
print("5-salir")
opcion = int(input("introduce la operacion que desea realizar : "))
if (opcion == 1):
    operacion = num1 + num2
    print(operacion)
elif (opcion == 2):
    operacion = num1 - num2
    print(operacion)
elif (opcion == 3):
    operacion = num1 * num2
    print(operacion)
elif (opcion == 4):
    operacion = num1 / num2
    print(operacion)
elif (opcion == 5):
    print("adios")
else :
    print("introduce una opcion valida")
