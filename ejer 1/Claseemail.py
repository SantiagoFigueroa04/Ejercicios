class Email:    #Clase Email
    __idCuenta= ""
    __dominio= ""           #Atributos de la Clase Email
    __tipoDom= ""
    __contraseña = ""
    
    def __init__(self, id,dom,tipo,contra): #Contructor con 4 argumentos para inicializar
        self.__idCuenta = id
        self.__dominio = dom
        self.__tipoDom = tipo
        self.__contraseña = contra

    def retornarEmail(self):    #Metodo de la Clase Email (crea el gmail a partir de los atributos asignados)
         gmail= self.__idCuenta+"@"+self.__dominio+"."+self.__tipoDom 
         return gmail
    
    def getDominio(self):       #Metodo de la Clase Email (retorna el email)
        return self.__dominio
    
    def getContraseña(self):      #Metodo para Retornar la contraseña   
        return self.__contraseña
    
    def setContraseña(self,nueva): #Metodo para modificar la contraseña
        self.__contraseña = nueva  