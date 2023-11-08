#escribir variables
#variable para guardar la contraseña
contraseña = "python"
#guardamos en memoria la contraseña
contraseña_introducida = input("introduce la contraseña:")
#convertimos la contraseña introducida a minuscula
introducida = contraseña_introducida.lower()
#comparamos las contraseñas
if contraseña == contraseña_introducida:
    print("contraseña correcta.")
else :
    print("contraseña incorrecta.")
