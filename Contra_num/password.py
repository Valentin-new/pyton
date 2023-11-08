#Almacenamos la contraseña valida
password = "1234567"
#Introsudimos la contraseña
password_introducida = input("Introduzca la contraseña")
#Comprobar si la contraseña
if password_introducida == password:
    print("contraseña correcta")
else:
    print("Contraseña incorrecta")