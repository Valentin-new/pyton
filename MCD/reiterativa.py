#base exponente
def potencia(base,exp):
    if exp ==0:
        return 1
    return base * potencia (base,exp-1)



def main():
    base = int(input("introduce la base: "))
    exp = int(input("introduce el exonente: "))
    print(base,"elevado a ",exp," es ",potencia(base,exp))


main()