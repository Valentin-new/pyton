#Escribe un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña

#almacenamos la contreseña válida
password = "Holi"
#introducimos por teclado la contraseña
contrasena_introducida = input("Introduce la contraseña: ")
while password != contrasena_introducida:
    contraseña_introducida = input("Error: Vuelve a introducir la contraseña válida")
print("Contraseña válida")