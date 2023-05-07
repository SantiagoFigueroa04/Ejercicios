class Conjunto:
    def __init__(self, *elementos):
        self.__elementos = set(elementos)
    # * Almacena cualquier cantidad de elementos

    def __add__(self, otro):
        return Conjunto(*(self.__elementos | otro.__elementos))
    #Se utiliza el operador | para calcular la unión de los conjuntos

    def __sub__(self, otro):
        return Conjunto(*(self.__elementos - otro.__elementos))

    def __eq__(self, otro):
          return sorted(self.__elementos) == sorted(otro.__elementos)
    
    def __str__(self):
        return str(self.__elementos)
    