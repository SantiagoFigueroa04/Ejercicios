from LeerArchivo import LeerArchivo
from maximo import maximo
from AcumularMillas import acumularmillas
from CanjearMillas import canjearmillas
from ClassViajero2 import ViajeroFrecuente

if __name__=="__main__":
    Lista=[]
    LeerArchivo(Lista)
    maximo(Lista)
    acumularmillas(Lista)
    canjearmillas(Lista)
