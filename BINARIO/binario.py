def intro_num():
    return int(input("Inroduce un numero entero"))

def binario(num):
    if num == 2:
        return 1
    elif num>2:
        return binario(num/2,)
    else:
        return 1
def main():
   print("introduce el primer numero")
   num = intro_num()

   print("El resultado es: ", binario(num))

main()