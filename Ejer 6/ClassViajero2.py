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
    
    def __gt__(self, otro):
        return self.__millasacum > otro.__millasacum
    
    def getnom(self):
        return self.__nombre
    
    def __add__(self, millas):
        return ViajeroFrecuente(0,"","","",self.__millasacum+millas)
    def __sub__(self, millas):
        return ViajeroFrecuente(0,"","","",self.__millasacum-millas)
    
    def __str__(self):
        return f"Viajero {self.__nombre} {self.__apellido}, DNI: {self.__dni}, Millas acumuladas: {self.__millasacum}"