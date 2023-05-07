#--------------Programa Principal----------
from Claseemail import Email
from CargarLista import cargar
from CrearEmail import crearGmail
from EnviarMsj import enviarMsj
if __name__ == '__main__': #Inicio del programa
    listadeGmail=[]  
    cargar(listadeGmail)
    indice = enviarMsj(listadeGmail)
