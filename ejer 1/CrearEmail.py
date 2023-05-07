from Claseemail import Email
def crearGmail():   #Funcion para inicializar las intancias de la clase Email
    print("Ingrese los siguientes datos:")
    id= str(input("Id: "))
    dom=input("dominio: ")
    tipo=input("tipo de dominio: ")
    contra=input("contraseña: ")
    email= Email(id,dom,tipo,contra) #aqui creamos el objecto, lo guardamos en una variable y lo retornamos
    return email