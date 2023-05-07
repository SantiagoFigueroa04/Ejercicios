import csv
from ClasePlanAhorro import PlanAhorro
def LeerArchivo(Lista):
    archivo=open("C:\\Users\\augus\\Downloads\\Nueva carpeta\\Ejer5\\planes(1).csv")
    reader=csv.reader(archivo,delimiter=";")
    for i in reader:
        cod=i[0]
        mod=i[1]
        vers=i[2]
        val=i[3]
        cuotasP=i[4]
        cuotasL=i[5]
        Plan=PlanAhorro(cod, mod, vers, val, cuotasP, cuotasL)
        Lista.append(Plan)
    archivo.close()
