import csv
class ViajeroFrecuente:
    __num_viajero=0
    __dni=""
    __nombre=""
    __apellido=""
    __millasacum=0

    def __init__(self, num, dni, nombre, ape, millas):
        self.__num_viajero=num
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=ape
        self.__millasacum=int(millas) 

    def getnum(self):
        return self.__num_viajero
    
    def cantidadTotalMillas(self):
        return self.__millasacum
    
    def __eq__(self, otro):
        return self.__millasacum==otro
    
    def __radd__(self, otro):
        return ViajeroFrecuente(0,"","","",self.__millasacum+otro)
    
    def getnom(self):
        return self.__nombre
    
    def __rsub__(self,otro):
        return self.__millasacum-otro

    def __str__(self):
        return "Millas acumuladas: {}".format(self.__millasacum)
