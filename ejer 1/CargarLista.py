from CrearEmail import crearGmail
def cargar(l):  #Funcion para crear la cantidad de objetos a crear
    cant=int(input("Ingrese la cantidad de gmails a cargar: ")) #pido el tamaño de la lista
    for i in range(cant):
        gmail = crearGmail()
        l.append(gmail)
    print("Datos cargado con exito!")
    print()
