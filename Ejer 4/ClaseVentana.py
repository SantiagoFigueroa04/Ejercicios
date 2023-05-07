class Ventana:
    __titulo=""
    __ValorCordenadaX_VSI=0
    __ValorCordenadaY_VSI=0
    __ValorCordenadaX_VID=0
    __ValorCordenadaY_VID=0
    
    def __init__(self, titulo, x=0, y=0, xdos=500, ydos=500):
         self.__titulo=titulo
         self.__ValorCordenadaX_VSI=x
         self.__ValorCordenadaY_VSI=y
         self.__ValorCordenadaX_VID=xdos
         self.__ValorCordenadaY_VID=ydos
         
    def mostrar(self):
        print ("Ejes del Vértice superior Izq=[{},{}]\nEjes del Vértice inferior derecho=[{},{}]".format (self.__ValorCordenadaX_VSI, self.__ValorCordenadaY_VSI, self.__ValorCordenadaX_VID, self.__ValorCordenadaY_VID))
    
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return self.__ValorCordenadaY_VSI
    def ancho(self):
        return self.__ValorCordenadaY_VID
    
    def moverDerecha(self,x):
        Pos=x+self.__ValorCordenadaX_VSI
        if Pos<=500:
            self.__ValorCordenadaX_VSI+=x
        else:
            print("No es posible moverse a la derecha")
        
    def moverIzquierda(self, x):
        pos=x-self.__ValorCordenadaX_VSI
        if(pos>=0):
            self.__ValorCordenadaX_VSI-=x
        else:
                print("No es posible moverse a la izquierda")
    
    def bajar(self, y):
        pos=y-self.__ValorCordenadaX_VSI
        if pos<=500:
          self.__ValorCordenadaY_VID-=y
        else:
          print("No es posible bajar")
        
    def subir(self, y):
        pos=y+self.__ValorCordenadaX_VSI
        if pos>=0:
          self.__ValorCordenadaY_VID-=y
        else:
          print("No es posible subir")
        