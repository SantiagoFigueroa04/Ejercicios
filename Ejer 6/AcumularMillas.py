def acumularmillas(Lista):
    num=input("Ingrese numero de viajero al que desea acumular millas: ")
    for i in range(len(Lista)):
        if(num==Lista[i].getnum()):
            millas=int(input("Ingrese millas que desea acumular: "))
            sum=Lista[i]+millas