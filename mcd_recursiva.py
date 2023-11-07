def intro_num():
    return int(input("Inroduce un numero entero"))

def mcd(num1,num2):
    if num1 == num2:
        return num1
    elif num1>num2:
        return mcd(num1-num2,num2)
    else:
        return mcd(num1, num2-num1)

def main():
    print("introduce el primer numero")
    num1 = intro_num()
    print("introduce el segundo numero")
    num2 = intro_num()
    print("El resultado es: ", mcd(num1,num2))

main()