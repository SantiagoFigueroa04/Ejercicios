
class PlanAhorro:
    __codPlan=0
    __modelo=""
    __version=""
    __valor=0.00
    __cantcuotasPlan=12
    __cantcuotasLicitar=6

    def __init__(self, cod, mod, vers, val, cuotasP, cuotasL):
     self.__codPlan=int(cod)
     self.__modelo=mod
     self.__version=vers
     self.__valor=float(val)
     self.__cantcuotasPlan=int(cuotasP)
     self.__cantcuotasLicitar=int(cuotasL)

    
    def getCodPlan(self):
        return self.__codPlan
    def getModelo(self):
        return self.__modelo
    def getVersion(self):
        return self.__version
    def nuevoValor(self, val):
        self.__valor=val
        return self.__valor
    def getvalor (self):
        return self.__valor
    def getCuotasLicitar(self):
        return self.__cantcuotasLicitar
    def getCuotasPlan (self):
        return self.__cantcuotasPlan
    def NuevaCuotaLicitar(self, cuota):
        self.__cantcuotasLicitar=cuota
        return self.__cantcuotasLicitar
    
    
