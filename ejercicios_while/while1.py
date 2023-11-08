#Visualizar en pantalla la suma y producto de los números
#inicializamos los acumuladores
suma = 0
producto = 1
cont = 1
# Mientras que el contador sea menor o igual a 3
while cont <= 3:
    suma = suma + cont
    producto = producto * cont
    cont = cont + 1
#Visiualizamos en pantalla los resultados
print("suma =", suma)
print("Producto=", producto)
print("Fin del programa")
#