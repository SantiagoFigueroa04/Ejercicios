def canjearmillas(Lista):
    num=input("Ingrese numero de viajero al que desea canjear sus millas: ")
    for i in range(len(Lista)):
        if(num==Lista[i].getnum()):
            millas=int(input("Ingrese millas que desea canjear: "))
            if (millas<=Lista[i].cantidadTotalMillas()):
                resta=Lista[i]-millas