import Claseemail as clase
import csv

def LeerArchivos():
    band = True
    archivos = open("C:\\Users\\augus\Downloads\\Nueva carpeta\\ejer 1\\ArchivoEmail.csv")
    reader= csv.reader(archivos,delimiter=";")
    for i in reader:
        if band:
            band = False
        else:
            nuevo = clase.Email("","","","")
            correo = nuevo.retornaEmail()
            contraseña=i[3]
            nuevo.crearCuenta(correo,contraseña)
    archivos.close  