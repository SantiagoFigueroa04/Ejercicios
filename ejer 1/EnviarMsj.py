import Claseemail
def enviarMsj(l): #Funcion para emitir un msj (insiso 1)
    nombre=input("ingrese su nombre: ")
    gmail=input("Ingrese su correo electronico: ")
    band=True
    for i in range(len(l)):
        if(l[i].retornarEmail() == gmail ):
            band=False #para saber si encontro el gmail
            indice = i #para el insiso 2
    if(band == False):
        print("Estimado:", nombre, "te enviaremos tus mensajes a la direccion", gmail)
        print("--Proceso de Modificacion--") #  <------Insiso 2 
        contra=input("Ingrese la contraseña actual: ")
        if(contra == l[i].getContraseña()):
            nueva=input("Ahora ingrese la contraseña nueva: ")
            l[i].setContraseña(nueva)
            print("Contraseña nueva --->", l[i].getContraseña(),"  Modificada con exito!")
        else:
            print("Contraseña Incorrecta.")
    else:
        print("El correo ingresado es invalido!")
 