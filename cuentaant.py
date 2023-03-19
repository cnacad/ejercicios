
class cuenta(): 
    def __init__(self,titular): 
        self.__titular = titular
        self.__cantidad= 0.0
                
    @property        
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
        
    @property        
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter    
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        return self.__cantidad

    def ingresar(self,cantidadIngreso):
        if (cantidadIngreso>0):
            self.__cantidad = self.__cantidad+cantidadIngreso

    def retirar(self,cantidadRetiro):
        self.__cantidad=self.__cantidad-cantidadRetiro

