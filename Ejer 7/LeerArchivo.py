import csv
from ClaseViajero3 import ViajeroFrecuente
def LeerArchivo(Lista):
    archivo=open("C:\\Users\\augus\\Downloads\\Nueva carpeta\\Ejer 7\\Viajeros.csv")
    reader=csv.reader(archivo,delimiter=",")
    bandera=True
    for i in reader:
        if bandera:
            bandera=False
        else:
            num=i[0]
            dni=i[1]
            nombre=i[2]
            ape=i[3]
            millas=i[4]
            viajero=ViajeroFrecuente(num, dni, nombre, ape, millas)
            Lista.append(viajero)
    archivo.close()