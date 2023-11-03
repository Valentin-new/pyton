#Hacemos el algoritmo del minimo común divisor

def mcd(num1,num2):
    while(num1 != num2):
        if (num1>num2):
            num1 = num1 - num2
        else:
            num2 = num2-num1
    return num1


def main():
    num1 =int(input("introduce el numero uno: "))
    num2 = int(input("introduce el numero dos: "))
    print("El mazimo comun divisor es: ",mcd(num1,num2))



main()